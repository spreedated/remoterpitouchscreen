Public Class Main
    Public isClosing As Boolean = False

    Private Sub Main_Load(sender As Object, e As EventArgs) Handles MyBase.Load
#If DEBUG Then
        Btn_Debug.Visible = True
#Else
        btn_Debug.Visible = False
#End If

        Mod_AppProperties.SetSettings(Me)
        Mod_StatusStrip.ReadyStrip()
        InitializeServer()
    End Sub

#If DEBUG Then
    Private Sub Btn_Debug_Click(sender As Object, e As EventArgs) Handles Btn_Debug.Click

    End Sub
#End If

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
