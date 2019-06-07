Module Mod_StatusStrip
    Public Sub ReadyStrip()
        Main.statIcon.Text = "-"
        Main.statText.Text = "Ready..."
    End Sub
    Public Sub ErrorStrip(ByVal Optional errorText As String = Nothing)
        Main.statIcon.Text = "-"
        If errorText = Nothing Then
            Main.statText.Text = "Something went wrong..."
        Else
            Main.statText.Text = "Error: " & errorText
        End If
    End Sub
    Public Sub WorkingAniStrip(ByVal state As Boolean)
        Select Case state
            Case True
                With AnimationTimer
                    .Enabled = True
                    .Interval = 100
                    .Start()
                End With
            Case False
                If AnimationTimer.Enabled Then
                    With AnimationTimer
                        .Enabled = False
                        .Stop()
                    End With
                End If
        End Select
    End Sub
    Private ReadOnly animationStates As String() = {"|", "/", "-", "|", "\"}
    Private animationPos As Short = 0
    Private WithEvents AnimationTimer As Timer = New Timer
    Private Sub AnimationTimer_Tick() Handles AnimationTimer.Tick
        Main.statIcon.Text = animationStates(animationPos)
        animationPos += 1
        If animationPos > (animationStates.Length - 1) Then
            animationPos = 0
        End If
    End Sub
End Module
