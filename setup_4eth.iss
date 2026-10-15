[Setup]
AppId=ShanheRiverEchoes4Eth-CustomByStudent2026
AppName=山河回响（四族定制版）
AppVersion=1.0.0
AppPublisher=云南大学 AI与社会科学 课程作业
DefaultDirName={localappdata}\Programs\ShanheRiverEchoes4Eth
PrivilegesRequired=lowest
DefaultGroupName=山河回响（四族定制版）
OutputDir=installer_output
OutputBaseFilename=山河回响_四族定制版_Setup
Compression=lzma2/max
SolidCompression=yes
UninstallDisplayIcon={app}\山河回响.exe
WizardStyle=modern

[Files]
Source: "D:\伟华老师AI\shanhe_build\mountainriverechoes\dist_4eth_new\山河回响\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion
Source: "D:\伟华老师AI\shanhe_build\assets\yt-dlp.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\山河回响（四族定制版）"; Filename: "{app}\山河回响.exe"; WorkingDir: "{app}"
Name: "{autodesktop}\山河回响（四族定制版）"; Filename: "{app}\山河回响.exe"; WorkingDir: "{app}"

[Run]
Filename: "{app}\山河回响.exe"; Description: "立即启动山河回响"; Flags: nowait postinstall skipifsilent
