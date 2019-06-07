''' <summary>
''' Version: v0.5
''' by Markus Karl Wackermann
''' </summary>
Module Mod_AppProperties
    Private ReadOnly AppNameWithoutVersion As String = My.Application.Info.Title

    Private Function AppName() As String
        Return AppNameWithoutVersion & " v" & AppVersionToString()
    End Function

    Private Function AppVersionToString() As String
        Dim acc As String = My.Application.Info.Version.ToString
        acc = acc.TrimEnd(".")

        'If ends with ZERO -> DELETE
        Do Until Not acc.EndsWith("0")
            If acc.EndsWith("0") Then
                acc = acc.Substring(0, acc.LastIndexOf("."))
                acc = acc.TrimEnd(".")
            End If
        Loop

        Return acc
    End Function

    Public Function SetSettings(ByRef Form As Form)
        With Form
            .Text = AppName()
            .Icon = My.Resources.icon
        End With

        Return True
    End Function
End Module
