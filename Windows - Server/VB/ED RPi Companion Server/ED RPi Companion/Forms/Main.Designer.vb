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
        Me.Button1 = New System.Windows.Forms.Button()
        Me.CheckBox1 = New System.Windows.Forms.CheckBox()
        Me.StatusStrip1 = New System.Windows.Forms.StatusStrip()
        Me.statIcon = New System.Windows.Forms.ToolStripStatusLabel()
        Me.statText = New System.Windows.Forms.ToolStripStatusLabel()
        Me.statBracketOpen = New System.Windows.Forms.ToolStripStatusLabel()
        Me.statBracketClose = New System.Windows.Forms.ToolStripStatusLabel()
        Me.StatusStrip1.SuspendLayout()
        Me.SuspendLayout()
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(308, 79)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(51, 25)
        Me.Button1.TabIndex = 0
        Me.Button1.Text = "Button1"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'CheckBox1
        '
        Me.CheckBox1.AutoSize = True
        Me.CheckBox1.Location = New System.Drawing.Point(163, 20)
        Me.CheckBox1.Name = "CheckBox1"
        Me.CheckBox1.Size = New System.Drawing.Size(112, 17)
        Me.CheckBox1.TabIndex = 1
        Me.CheckBox1.Text = "Advertising Server"
        Me.CheckBox1.UseVisualStyleBackColor = True
        '
        'StatusStrip1
        '
        Me.StatusStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.statBracketOpen, Me.statIcon, Me.statBracketClose, Me.statText})
        Me.StatusStrip1.Location = New System.Drawing.Point(0, 151)
        Me.StatusStrip1.Name = "StatusStrip1"
        Me.StatusStrip1.Size = New System.Drawing.Size(673, 22)
        Me.StatusStrip1.TabIndex = 2
        Me.StatusStrip1.Text = "StatusStrip1"
        '
        'statIcon
        '
        Me.statIcon.AutoSize = False
        Me.statIcon.Name = "statIcon"
        Me.statIcon.Size = New System.Drawing.Size(10, 17)
        Me.statIcon.Text = "+"
        '
        'statText
        '
        Me.statText.Name = "statText"
        Me.statText.Size = New System.Drawing.Size(120, 17)
        Me.statText.Text = "ToolStripStatusLabel2"
        '
        'statBracketOpen
        '
        Me.statBracketOpen.AutoSize = False
        Me.statBracketOpen.Name = "statBracketOpen"
        Me.statBracketOpen.Size = New System.Drawing.Size(10, 17)
        Me.statBracketOpen.Text = "["
        '
        'statBracketClose
        '
        Me.statBracketClose.AutoSize = False
        Me.statBracketClose.Name = "statBracketClose"
        Me.statBracketClose.Size = New System.Drawing.Size(10, 17)
        Me.statBracketClose.Text = "]"
        '
        'Main
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(673, 173)
        Me.Controls.Add(Me.StatusStrip1)
        Me.Controls.Add(Me.CheckBox1)
        Me.Controls.Add(Me.Button1)
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

    Friend WithEvents Button1 As Button
    Friend WithEvents CheckBox1 As CheckBox
    Friend WithEvents StatusStrip1 As StatusStrip
    Friend WithEvents statIcon As ToolStripStatusLabel
    Friend WithEvents statText As ToolStripStatusLabel
    Friend WithEvents statBracketOpen As ToolStripStatusLabel
    Friend WithEvents statBracketClose As ToolStripStatusLabel
End Class
