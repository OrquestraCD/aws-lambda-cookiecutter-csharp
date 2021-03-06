#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.use_kms }}' == 'NO':
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "src/Adapters/SecretManagement.Adapter"))
        remove_file("src/Core/Ports/ISecretManagementService.cs")
