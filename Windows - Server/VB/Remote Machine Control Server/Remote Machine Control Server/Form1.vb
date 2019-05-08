Imports System.Net
Imports System.Net.Sockets
Imports System.Text


Public Class Form1
    Private UDPClient As UdpClient = New UdpClient()

    Private backT As Threading.Thread

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        backT = New Threading.Thread(Sub() BackThread())

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Select Case backT.IsAlive
            Case True
                backT.Suspend()
            Case False
                Try
                    backT.Resume()

                Catch ex As Exception
                    backT.Start()
                End Try
        End Select
    End Sub


    Private Sub BackThread()
        Try
            Dim myip As IPAddress = IPAddress.Parse("192.168.1.137")

            UDPClient.Client.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReuseAddress, True)
            UDPClient.Client.Bind(New IPEndPoint(myip, 15548))

            Dim iepRemoteEndPoint As IPEndPoint = New IPEndPoint(myip, 15548)

            Do
                Dim bytRecieved As Byte() = UDPClient.Receive(iepRemoteEndPoint)
                Dim strMessage = Encoding.ASCII.GetString(bytRecieved)

                Debug.Print("Msg: " & strMessage)
            Loop


        Catch ex As Exception

        Finally
            UDPClient.Close()
        End Try
    End Sub
End Class
