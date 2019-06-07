<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Main
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.Btn_Debug = New System.Windows.Forms.Button()
        Me.CheckBox1 = New System.Windows.Forms.CheckBox()
        Me.StatusStrip1 = New System.Windows.Forms.StatusStrip()
        Me.statBracketOpen = New System.Windows.Forms.ToolStripStatusLabel()
        Me.statIcon = New System.Windows.Forms.ToolStripStatusLabel()
        Me.statBracketClose = New System.Windows.Forms.ToolStripStatusLabel()
        Me.statText = New System.Windows.Forms.ToolStripStatusLabel()
        Me.Log_Box = New System.Windows.Forms.RichTextBox()
        Me.StatusStrip1.SuspendLayout()
        Me.SuspendLayout()
        '
        'Btn_Debug
        '
        Me.Btn_Debug.Location = New System.Drawing.Point(122, 12)
        Me.Btn_Debug.Name = "Btn_Debug"
        Me.Btn_Debug.Size = New System.Drawing.Size(64, 26)
        Me.Btn_Debug.TabIndex = 0
        Me.Btn_Debug.Text = "Debug"
        Me.Btn_Debug.UseVisualStyleBackColor = True
        '
        'CheckBox1
        '
        Me.CheckBox1.AutoSize = True
        Me.CheckBox1.Location = New System.Drawing.Point(12, 12)
        Me.CheckBox1.Name = "CheckBox1"
        Me.CheckBox1.Size = New System.Drawing.Size(104, 17)
        Me.CheckBox1.TabIndex = 1
        Me.CheckBox1.Text = "Advertise Server"
        Me.CheckBox1.UseVisualStyleBackColor = True
        '
        'StatusStrip1
        '
        Me.StatusStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.statBracketOpen, Me.statIcon, Me.statBracketClose, Me.statText})
        Me.StatusStrip1.Location = New System.Drawing.Point(0, 206)
        Me.StatusStrip1.Name = "StatusStrip1"
        Me.StatusStrip1.Size = New System.Drawing.Size(279, 22)
        Me.StatusStrip1.TabIndex = 2
        Me.StatusStrip1.Text = "StatusStrip1"
        '
        'statBracketOpen
        '
        Me.statBracketOpen.AutoSize = False
        Me.statBracketOpen.Name = "statBracketOpen"
        Me.statBracketOpen.Size = New System.Drawing.Size(10, 17)
        Me.statBracketOpen.Text = "["
        '
        'statIcon
        '
        Me.statIcon.AutoSize = False
        Me.statIcon.Name = "statIcon"
        Me.statIcon.Size = New System.Drawing.Size(10, 17)
        Me.statIcon.Text = "+"
        '
        'statBracketClose
        '
        Me.statBracketClose.AutoSize = False
        Me.statBracketClose.Name = "statBracketClose"
        Me.statBracketClose.Size = New System.Drawing.Size(10, 17)
        Me.statBracketClose.Text = "]"
        '
        'statText
        '
        Me.statText.Name = "statText"
        Me.statText.Size = New System.Drawing.Size(120, 17)
        Me.statText.Text = "ToolStripStatusLabel2"
        '
        'Log_Box
        '
        Me.Log_Box.BorderStyle = System.Windows.Forms.BorderStyle.None
        Me.Log_Box.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.Log_Box.DetectUrls = False
        Me.Log_Box.Location = New System.Drawing.Point(12, 50)
        Me.Log_Box.Name = "Log_Box"
        Me.Log_Box.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.Vertical
        Me.Log_Box.ShortcutsEnabled = False
        Me.Log_Box.Size = New System.Drawing.Size(255, 144)
        Me.Log_Box.TabIndex = 3
        Me.Log_Box.Text = ""
        '
        'Main
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(279, 228)
        Me.Controls.Add(Me.Log_Box)
        Me.Controls.Add(Me.StatusStrip1)
        Me.Controls.Add(Me.CheckBox1)
        Me.Controls.Add(Me.Btn_Debug)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle
        Me.MaximizeBox = False
        Me.Name = "Main"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        Me.Text = "Main"
        Me.StatusStrip1.ResumeLayout(False)
        Me.StatusStrip1.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents Btn_Debug As Button
    Friend WithEvents CheckBox1 As CheckBox
    Friend WithEvents StatusStrip1 As StatusStrip
    Friend WithEvents statIcon As ToolStripStatusLabel
    Friend WithEvents statText As ToolStripStatusLabel
    Friend WithEvents statBracketOpen As ToolStripStatusLabel
    Friend WithEvents statBracketClose As ToolStripStatusLabel
    Friend WithEvents Log_Box As RichTextBox
End Class
