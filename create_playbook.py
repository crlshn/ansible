with open('commandos.txt', 'r') as f:
    commands = f.read().splitlines()

    with open('playbooks/comandos.yml', 'w') as playbook:
        playbook.write('- hosts: localhost\n')
        playbook.write('  gather_facts: false\n')
        playbook.write('  ignore_unreachable: true\n')
        playbook.write('  tasks:\n')
        for command in commands:
            command_no_spaces = command.replace(' ', '_').replace('-', '_').replace('|', '_')
            playbook.write(f'  - name: run {command} to gather evidence\n')
            playbook.write('    ignore_errors: true\n')
            playbook.write('    timeout: 3600\n')
            playbook.write('    poll: 10\n')
            playbook.write('    ios_command:\n')
            playbook.write('        commands: ' + command + '\n')
            playbook.write(f'    register: evidence_{command_no_spaces}\n')
        for command in commands:
            command_no_spaces = command.replace(' ', '_').replace('-', '_')
            playbook.write(f'  - name: display evidence {command}\n')
            playbook.write('    debug:\n')
            playbook.write(
                f'      var: evidence_{command_no_spaces}["stdout_lines"][0]\n')
