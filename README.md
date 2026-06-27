# Forensics_Tool
A tool that collects network/system data all together for forensics purposes.

## Overview

Forensics Tool is a Python-based endpoint forensic analysis platform developed to support digital investigations through automated evidence acquisition, system inspection, and artifact analysis. The project focuses on improving the speed, reliability, and scalability of forensic workflows across Windows endpoint environments.

## Core Capabilities

* Endpoint system analysis and forensic artifact collection
* Network activity and connection analysis
* Browser history and downloaded file inspection
* USB device and external storage tracking
* Windows Event Log and system timeline analysis
* Executable enumeration and malicious file detection
* Metadata extraction and filesystem inspection
* Automated forensic report generation

## Architecture

The application integrates multiple system-level and forensic analysis modules using Python libraries and Windows management interfaces. It leverages process monitoring, registry analysis, filesystem traversal, network inspection, and YARA-based signature matching to identify suspicious artifacts and support incident investigations.

## Technologies Used

* Python
* WMI
* psutil
* YARA
* SQLite3
* WinReg
* Socket Programming

## Project Objective

The project aims to modernize endpoint forensic investigations by automating repetitive analysis tasks, reducing investigation time, and improving the accuracy of digital evidence collection and interpretation across complex endpoint systems.

## Scope

The tool is designed for cybersecurity research, forensic analysis, and educational applications involving endpoint monitoring, artifact analysis, and incident response workflows.

## Disclaimer

This project was originally developed in 2023 and reflects the scope, architecture, and implementation state from that period. While the overall concept and forensic workflow remain relevant, several components can be further modernized and extended.

This repository currently contains the portion of the project contributed and maintained by the author, rather than the complete original application. As a result, the repository is not yet fully execution-ready for public deployment or end-to-end usage.

The current version is primarily optimized for Windows environments and Linux, but has not yet been fully adapted or tested for macOS compatibility.

Ongoing work is focused on refactoring, improving compatibility, and packaging the project into a fully executable and reproducible forensic analysis tool for broader accessibility and testing.
