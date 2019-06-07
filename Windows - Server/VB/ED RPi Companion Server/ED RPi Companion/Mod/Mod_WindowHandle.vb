Imports System.Runtime.InteropServices
Imports System.Text

Module Mod_WindowHandle
    <DllImport("user32.dll", CharSet:=CharSet.Auto, SetLastError:=True)>
    Private Function GetForegroundWindow() As IntPtr
    End Function
    <DllImport("user32.dll", CharSet:=CharSet.Auto, SetLastError:=True)>
    Private Function GetWindowText(hWnd As IntPtr, text As StringBuilder, count As Integer) As Integer
    End Function
    <DllImport("user32.dll", CharSet:=CharSet.Auto, SetLastError:=True)>
    Private Function GetWindowTextLength(hWnd As IntPtr) As Integer
    End Function
    Public Function GetCaptionOfActiveWindow() As String
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
End Module
