[Setup]
AppId=ShanheRiverEchoes4Single-CustomByStudent2026
AppName=山河回响（四族独立版）
AppVersion=2.0.0
AppPublisher=云南大学 AI与社会科学 课程作业
DefaultDirName={localappdata}\Programs\ShanheRiverEchoes4Single
PrivilegesRequired=lowest
DefaultGroupName=山河回响（四族独立版）
OutputDir=installer_output
OutputBaseFilename=山河回响_四族独立版_Setup
Compression=lzma2/max
SolidCompression=yes
UninstallDisplayIcon={app}\山河回响-毛南族\山河回响-毛南族.exe
WizardStyle=modern

[Files]
Source: "D:\伟华老师AI\shanhe_build\mountainriverechoes\dist_single_new\山河回响-毛南族\*"; DestDir: "{app}\山河回响-毛南族"; Flags: recursesubdirs createallsubdirs ignoreversion
Source: "D:\伟华老师AI\shanhe_build\mountainriverechoes\dist_single_new\山河回响-仡佬族\*"; DestDir: "{app}\山河回响-仡佬族"; Flags: recursesubdirs createallsubdirs ignoreversion
Source: "D:\伟华老师AI\shanhe_build\mountainriverechoes\dist_single_new\山河回响-锡伯族\*"; DestDir: "{app}\山河回响-锡伯族"; Flags: recursesubdirs createallsubdirs ignoreversion
Source: "D:\伟华老师AI\shanhe_build\mountainriverechoes\dist_single_new\山河回响-独龙族\*"; DestDir: "{app}\山河回响-独龙族"; Flags: recursesubdirs createallsubdirs ignoreversion
Source: "D:\伟华老师AI\shanhe_build\assets\yt-dlp.exe"; DestDir: "{app}\山河回响-毛南族"; Flags: ignoreversion
Source: "D:\伟华老师AI\shanhe_build\assets\yt-dlp.exe"; DestDir: "{app}\山河回响-仡佬族"; Flags: ignoreversion
Source: "D:\伟华老师AI\shanhe_build\assets\yt-dlp.exe"; DestDir: "{app}\山河回响-锡伯族"; Flags: ignoreversion
Source: "D:\伟华老师AI\shanhe_build\assets\yt-dlp.exe"; DestDir: "{app}\山河回响-独龙族"; Flags: ignoreversion

[Icons]
Name: "{autodesktop}\山河回响·毛南族"; Filename: "{app}\山河回响-毛南族\山河回响-毛南族.exe"; WorkingDir: "{app}\山河回响-毛南族"
Name: "{autodesktop}\山河回响·仡佬族"; Filename: "{app}\山河回响-仡佬族\山河回响-仡佬族.exe"; WorkingDir: "{app}\山河回响-仡佬族"
Name: "{autodesktop}\山河回响·锡伯族"; Filename: "{app}\山河回响-锡伯族\山河回响-锡伯族.exe"; WorkingDir: "{app}\山河回响-锡伯族"
Name: "{autodesktop}\山河回响·独龙族"; Filename: "{app}\山河回响-独龙族\山河回响-独龙族.exe"; WorkingDir: "{app}\山河回响-独龙族"
