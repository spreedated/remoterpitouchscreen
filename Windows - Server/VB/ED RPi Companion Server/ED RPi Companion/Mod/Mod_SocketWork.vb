Imports System.Text
Imports System.Net
Imports System.Net.Sockets
Imports WindowsInput

Module Mod_SocketWork
    Public receivingClient As UdpClient
    Public sendingClient As UdpClient
    Public receivingThread As Threading.Thread
    Public sendingThread As Threading.Thread

    Public Sub InitializeAdvertising()
        sendingClient = New UdpClient("255.255.255.255", My.Settings.port) With {
            .EnableBroadcast = True
        }
        sendingThread = New Threading.Thread(AddressOf Advertiser) With {
            .IsBackground = True
        }
        sendingThread.Start()
    End Sub

    Public Sub InitializeServer()
        Try
            receivingClient = New UdpClient()
            receivingThread = New Threading.Thread(AddressOf Receiver) With {
                .IsBackground = True
            }
            receivingThread.Start()
            Mod_StatusStrip.WorkingAniStrip(True, "Listening on port " & My.Settings.port)
        Catch ex As Exception
            Debug.Print(ex.Message)
        End Try
    End Sub

    Private Sub Advertiser()
        Try
            Dim strMessage = "ADVERTISING#E:D RPi Companion .NET Server#0.1"
            Dim data() As Byte = Encoding.ASCII.GetBytes(strMessage)

            While True
                sendingClient.Send(data, data.Length)
                Threading.Thread.Sleep(My.Settings.advertisingInterval)
                Debug.Print("Send advert")
            End While
        Catch ex As Exception
            Debug.Print(ex.Message)
        End Try
    End Sub

    Private Sub Receiver()
        Dim iepRemoteEndPoint As IPEndPoint = New IPEndPoint(IPAddress.Any, My.Settings.port)

        'UDP Options
        receivingClient.Client.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReuseAddress, True) 'Allows the socket to be bound to an address that is already in use.
        receivingClient.Client.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReceiveTimeout, 0) 'Never timeout, listen while true is true, infinte

        receivingClient.Client.Bind(New IPEndPoint(IPAddress.Any, My.Settings.port)) 'Binds to any IP/NIC

        Try
#If DEBUG Then
            Debug.Print("Listening on port {0}", My.Settings.port.ToString)
#End If
            While True
                Dim data() As Byte
                data = receivingClient.Receive(iepRemoteEndPoint)
                Dim strMessage = Encoding.ASCII.GetString(data)

                If Not strMessage.StartsWith("ADVERTISING") Then
                    'Do Work
                    Debug.Print("rawMessage: " & strMessage)
                    If Mod_WindowHandle.GetCaptionOfActiveWindow().ToLower.Contains("elite") And Mod_WindowHandle.GetCaptionOfActiveWindow().ToLower.Contains("client") Then 'Check if ELITE Window is in focus
                        Dim split As String() = strMessage.Split("#")
                        Select Case split(0)
                            Case "key"
#If DEBUG Then
                                Dim raw As String = "rcvd : key : " & split(1)
#End If
                                Dim i = New InputSimulator
                                i.Keyboard.TextEntry(split(1))
                                Debug.Print(Mod_WindowHandle.GetCaptionOfActiveWindow())
                        End Select
                    End If
                End If
                If Main.isClosing Then
                    Exit Sub
                End If
            End While
        Catch ex As Exception
            Debug.Print(ex.Message)
        Finally
            receivingClient.Close()
        End Try
    End Sub
End Module
