Imports System.Net
Imports System.Net.Sockets
Imports System.Text
Imports System.Runtime.InteropServices
Imports Henooh.DeviceEmulator
Imports WindowsInput

Public Class Main
    <DllImport("user32.dll", CharSet:=CharSet.Auto, SetLastError:=True)>
    Private Shared Function GetForegroundWindow() As IntPtr
    End Function
    <DllImport("user32.dll", CharSet:=CharSet.Auto, SetLastError:=True)>
    Private Shared Function GetWindowText(hWnd As IntPtr, text As StringBuilder, count As Integer) As Integer
    End Function
    <DllImport("user32.dll", CharSet:=CharSet.Auto, SetLastError:=True)>
    Private Shared Function GetWindowTextLength(hWnd As IntPtr) As Integer
    End Function
    Private Function GetCaptionOfActiveWindow() As String
        Dim strTitle As String = String.Empty
        Dim handle As IntPtr = GetForegroundWindow()
        ' Obtain the length of the text   
        Dim intLength As Integer = GetWindowTextLength(handle) + 1
        Dim stringBuilder As New StringBuilder(intLength)
        If GetWindowText(handle, stringBuilder, intLength) > 0 Then
            strTitle = stringBuilder.ToString()
        End If
        Return strTitle
    End Function


    'Setup Vars
    Private receivingClient As UdpClient
    Private sendingClient As UdpClient
    Private receivingThread As Threading.Thread
    Private sendingThread As Threading.Thread
    Private isClosing As Boolean = False

    Private Sub Main_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Mod_AppProperties.SetSettings(Me)
        Mod_StatusStrip.ReadyStrip()
        InitializeServer()
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Select Case receivingThread.IsAlive
            Case True
                receivingThread.Abort()
            Case False
                InitializeServer()
        End Select
    End Sub

    Private Sub InitializeAdvertising()
        sendingClient = New UdpClient("255.255.255.255", My.Settings.port) With {
            .EnableBroadcast = True
        }
        sendingThread = New Threading.Thread(AddressOf Advertiser) With {
            .IsBackground = True
        }
        sendingThread.Start()
    End Sub

    Private Sub InitializeServer()
        Try
            receivingClient = New UdpClient()
            receivingThread = New Threading.Thread(AddressOf Receiver) With {
                .IsBackground = True
            }
            receivingThread.Start()
            Mod_StatusStrip.WorkingAniStrip(True)
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
            Debug.Print("Listening on port {0}", My.Settings.port.ToString)
            While True
                Dim data() As Byte
                data = receivingClient.Receive(iepRemoteEndPoint)
                Dim strMessage = Encoding.ASCII.GetString(data)

                If Not strMessage.StartsWith("ADVERTISING") Then
                    'Do Work
                    Debug.Print("rawMessage: " & strMessage)
                    If GetCaptionOfActiveWindow().ToLower.Contains("elite") And GetCaptionOfActiveWindow().ToLower.Contains("client") Then 'Check if ELITE Window is in focus
                        Dim split As String() = strMessage.Split("#")
                        Select Case split(0)
                            Case "key"
                                Debug.Print("rcvd : key : {0}", split(1))
                                Dim i = New InputSimulator
                                i.Keyboard.TextEntry(split(1))
                                Debug.Print(GetCaptionOfActiveWindow())
                        End Select
                    End If
                End If
                    If isClosing Then
                    Exit Sub
                End If
            End While
        Catch ex As Exception
            Debug.Print(ex.Message)
        Finally
            receivingClient.Close()
        End Try
    End Sub

    Private Sub Main_FormClosing(sender As Object, e As FormClosingEventArgs) Handles Me.FormClosing
        isClosing = True
        receivingClient.Close()
    End Sub

    Private Sub CheckBox1_CheckedChanged(sender As Object, e As EventArgs) Handles CheckBox1.CheckedChanged
        Dim obj As CheckBox = sender
        Select Case obj.CheckState
            Case CheckState.Checked
                InitializeAdvertising()
            Case CheckState.Unchecked
                If sendingThread.IsAlive Then
                    sendingThread.Abort()
                End If
        End Select
    End Sub
End Class
