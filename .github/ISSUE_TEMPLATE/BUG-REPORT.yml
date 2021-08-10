name: [BUG] Summary
description: Create a report to stamp out gzdoom rpm bugs
title: "[Bug] "
labels: bug
assignees:
  - nazunalika
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
  - type: textarea
    id: bug-description
    attributes:
      label: Describe the bug
      description: Describe the bug and tell us what you expected to happen instead
      placeholder: Details
    validations:
      required: false
  - type: textarea
    id: console-output
    attributes:
      label: Provide console output
      description: Provide console output if necessary. Otherwise, put N/A.
      placeholder: |
        # Examples
        % strace gzdoom
        . . .
        % gzdoom
        . . .
    validations:
      required: false
  - type: dropdown
    id: version
    attributes:
      label: Linux Version
      description: What supported distribution are you running?
      options:
        - Fedora 34 (default)
        - Fedora 33
        - Mageia (latest stable)
    validations:
      required: true
  - type: dropdown
    id: architecture
    attributes:
      label: What architecture are you running?
      multiple: true
      options:
        - x86_64
        - aarch64
        - ppc64le
  - type: textarea
    id: system-specs
    attributes:
      label: System Specifications
      description: Please provide your system specs. Sometimes it helps us to know what you're running.
      render: shell
  - type: textarea
    id: gzdoom-config
    attributes:
      label: gzdoom settings
      description: Please provide the wads and pk3's you are using for gzdoom, if applicable.
      render: shell
