VERSION 5.00
Begin VB.Form WangKe_Gui 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "�������ӻ�ȡ��_GUI"
   ClientHeight    =   5130
   ClientLeft      =   8130
   ClientTop       =   4785
   ClientWidth     =   13035
   DrawMode        =   12  'Nop
   FillStyle       =   2  'Horizontal Line
   BeginProperty Font 
      Name            =   "΢���ź�"
      Size            =   10.5
      Charset         =   134
      Weight          =   400
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   ForeColor       =   &H00000000&
   Icon            =   "WangKe_Gui.frx":0000
   LinkTopic       =   "GUI_Main"
   MaxButton       =   0   'False
   ScaleHeight     =   5130
   ScaleWidth      =   13035
   Begin VB.CommandButton Open_Mirror_Button 
      Appearance      =   0  'Flat
      Caption         =   "�����ξ���ַ�ƽ̨"
      Height          =   495
      Left            =   10440
      TabIndex        =   14
      Top             =   3960
      Width           =   2535
   End
   Begin VB.ComboBox exe_Path 
      Appearance      =   0  'Flat
      Height          =   420
      ItemData        =   "WangKe_Gui.frx":10CA
      Left            =   9480
      List            =   "WangKe_Gui.frx":10D4
      TabIndex        =   11
      Text            =   "�������ӻ�ȡ��_Ver1.7.exe"
      Top             =   360
      Width           =   3375
   End
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Left            =   8160
      Top             =   720
   End
   Begin VB.ComboBox Grades_Choice_List 
      Appearance      =   0  'Flat
      Height          =   420
      ItemData        =   "WangKe_Gui.frx":110E
      Left            =   10560
      List            =   "WangKe_Gui.frx":111E
      TabIndex        =   8
      Text            =   "��ѡ���꼶"
      Top             =   2280
      Width           =   2295
   End
   Begin VB.CommandButton Open_All_Link_Button 
      Appearance      =   0  'Flat
      Caption         =   "һ���򿪸��꼶���пγ�"
      Enabled         =   0   'False
      Height          =   495
      Left            =   10440
      TabIndex        =   7
      Top             =   2880
      Width           =   2535
   End
   Begin VB.CommandButton Load_Button 
      Appearance      =   0  'Flat
      Caption         =   "�������������б�"
      CausesValidation=   0   'False
      Height          =   495
      Left            =   10440
      TabIndex        =   6
      ToolTipText     =   "����Լ��������б�"
      Top             =   1680
      Width           =   2535
   End
   Begin VB.ListBox Link_list 
      Appearance      =   0  'Flat
      Height          =   3015
      IMEMode         =   2  'OFF
      IntegralHeight  =   0   'False
      ItemData        =   "WangKe_Gui.frx":1144
      Left            =   0
      List            =   "WangKe_Gui.frx":1146
      TabIndex        =   4
      Top             =   1560
      Width           =   10335
   End
   Begin VB.Label Title_shout 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      BeginProperty Font 
         Name            =   "΢���ź� Light"
         Size            =   18
         Charset         =   134
         Weight          =   290
         Underline       =   -1  'True
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00C00000&
      Height          =   615
      Left            =   0
      TabIndex        =   16
      Top             =   4560
      Width           =   12975
   End
   Begin VB.Label Label1 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "��������"
      Enabled         =   0   'False
      BeginProperty Font 
         Name            =   "΢���ź�"
         Size            =   12
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   375
      Left            =   11160
      TabIndex        =   15
      Top             =   3600
      Width           =   975
   End
   Begin VB.Label Title_Tips 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "����������������,���ֶ������ļ���"
      Enabled         =   0   'False
      ForeColor       =   &H80000008&
      Height          =   255
      Left            =   9480
      TabIndex        =   13
      Top             =   720
      Width           =   3495
   End
   Begin VB.Label Title_Choice_exe 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "��ѡ��������汾:"
      BeginProperty Font 
         Name            =   "΢���ź� Light"
         Size            =   14.25
         Charset         =   134
         Weight          =   290
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H000000FF&
      Height          =   375
      Left            =   9480
      TabIndex        =   12
      Top             =   0
      Width           =   3255
   End
   Begin VB.Label Warn 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "�����������˳���,����������ͬGUI����ͬһĿ¼��"
      BeginProperty Font 
         Name            =   "΢���ź� Light"
         Size            =   12
         Charset         =   134
         Weight          =   290
         Underline       =   -1  'True
         Italic          =   -1  'True
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H000000FF&
      Height          =   375
      Left            =   4560
      TabIndex        =   10
      Top             =   1200
      Width           =   5655
   End
   Begin VB.Label Title_Loading 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Enabled         =   0   'False
      BeginProperty Font 
         Name            =   "΢���ź�"
         Size            =   12
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   375
      Left            =   10440
      TabIndex        =   9
      Top             =   1320
      Width           =   2895
   End
   Begin VB.Label Title_3 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "���������б�˫���Դ�����"
      Enabled         =   0   'False
      BeginProperty Font 
         Name            =   "΢���ź�"
         Size            =   15
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   495
      Left            =   240
      TabIndex        =   5
      Top             =   1080
      Width           =   4695
   End
   Begin VB.Label BulidWith 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "BuildWith:Visual Basic 6.0"
      Enabled         =   0   'False
      ForeColor       =   &H80000008&
      Height          =   255
      Left            =   6600
      TabIndex        =   3
      Top             =   360
      Width           =   2655
   End
   Begin VB.Label Author 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "Author:2844829687@qq.com"
      Enabled         =   0   'False
      ForeColor       =   &H80000008&
      Height          =   300
      Left            =   6240
      TabIndex        =   2
      Top             =   120
      Width           =   2910
   End
   Begin VB.Label Title_2 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "���������GUI"
      Enabled         =   0   'False
      BeginProperty Font 
         Name            =   "΢���ź�"
         Size            =   12
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   315
      Left            =   6360
      TabIndex        =   1
      Top             =   720
      Width           =   1665
   End
   Begin VB.Label Title 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "�������ӻ�ȡ��"
      Enabled         =   0   'False
      BeginProperty Font 
         Name            =   "΢���ź�"
         Size            =   42
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   1095
      Left            =   240
      TabIndex        =   0
      Top             =   -120
      Width           =   5895
   End
End
Attribute VB_Name = "WangKe_Gui"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Public Shout_text As String
Public Link_1 As String
Public Link_2 As String
Public Link_3 As String
Public Link_4 As String
Public Link_5 As String
Public Link_6 As String
Public Link_7 As String
Private Sub Form_Load()
Shell "taskkill /f /im �������ӻ�ȡ��_Ver1.7.exe"
Shell "taskkill /f /im �������ӻ�ȡ��_Ver1.8.exe"
End Sub

Private Sub Open_All_Link_Button_Click()

Need_Open_URL_Grade_Num = Grades_Choice_List.ListIndex + 1

If Need_Open_URL_Grade_Num = 0 Then
MsgBox "����ѡ���꼶!"
End If

If Need_Open_URL_Grade_Num = 1 Then
Shell "explorer.exe " & Link_1
Shell "explorer.exe " & Link_2
End If

If Need_Open_URL_Grade_Num = 2 Then
Shell "explorer.exe " & Link_3
Shell "explorer.exe " & Link_4
End If

If Need_Open_URL_Grade_Num = 3 Then
Shell "explorer.exe " & Link_5
Shell "explorer.exe " & Link_6
Shell "explorer.exe " & Link_7
End If

If Need_Open_URL_Grade_Num = 3 Then
Shell "explorer.exe " & Link_1
Shell "explorer.exe " & Link_2
Shell "explorer.exe " & Link_3
Shell "explorer.exe " & Link_4
Shell "explorer.exe " & Link_5
Shell "explorer.exe " & Link_6
Shell "explorer.exe " & Link_7
End If

End Sub

Private Sub Open_Mirror_Button_Click()
Shell "explorer.exe https://yellow-stone.tpddns.cn:8000"
End Sub

Private Sub Timer1_Timer()

Link_list.Clear
Open "OutPut.txt" For Input As #1
n = 0

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 1 Then
Link_list.AddItem a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 2 Then
Link_list.AddItem a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 3 Then
Link_list.AddItem a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 4 Then
Link_list.AddItem a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 5 Then
Link_list.AddItem a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 6 Then
Link_list.AddItem a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 7 Then
Link_list.AddItem a
Exit Do
End If
Loop

'�����Ӳ���
Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 8 Then
Link_1 = a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 9 Then
Link_2 = a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 10 Then
Link_3 = a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 11 Then
Link_4 = a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 12 Then
Link_5 = a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 13 Then
Link_6 = a
Exit Do
End If
Loop

Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 14 Then
Link_7 = a
Exit Do
End If
Loop


Do While Not EOF(1)
Line Input #1, a
n = n + 1
If n = 15 Then
Shout_text = a
Exit Do
End If
Loop


Close #1

Timer1.Enabled = False
Load_Button.Enabled = True
Open_All_Link_Button.Enabled = True
Title_Loading.Caption = "�������!"

If Shout_text <> "" Then
Title_shout.Caption = "���߹���:" & Shout_text
End If

Kill "OutPut.txt"
End Sub
Private Sub Load_Button_Click()
exe_Path = exe_Path.Text
Title_Loading.Caption = "������,�����ĵȴ�20s"
Shell "" & exe_Path & " --no-window"
Timer1.Interval = 20000
Timer1.Enabled = True
Load_Button.Enabled = False

End Sub

Private Sub Link_list_DblClick()
Need_Open_URL_Num = Link_list.ListIndex + 1

If Need_Open_URL_Num = 1 Then
Need_Open_URL = Link_1
End If

If Need_Open_URL_Num = 2 Then
Need_Open_URL = Link_2
End If

If Need_Open_URL_Num = 3 Then
Need_Open_URL = Link_3
End If

If Need_Open_URL_Num = 4 Then
Need_Open_URL = Link_4
End If

If Need_Open_URL_Num = 5 Then
Need_Open_URL = Link_5
End If

If Need_Open_URL_Num = 6 Then
Need_Open_URL = Link_5
End If

If Need_Open_URL_Num = 7 Then
Need_Open_URL = Link_7
End If


Shell "explorer.exe " & Need_Open_URL
End Sub

