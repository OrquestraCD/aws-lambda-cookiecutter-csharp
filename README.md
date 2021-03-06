# Cookiecutter for AWS SAM and .NET

A Cookiecutter template to create a Serverless App based on Serverless Application Model (SAM) and .NET Core 2.1

> It is important to note that you should not try to `git clone` this project but use `sam` CLI instead as ``{{cookiecutter.project_slug}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

## Requirements

Install `aws-sam-cli` as described [in the documentation](https://hosting-and-deployment.office.coolblue.eu/#/aws/lambda/README?id=aws-sam-cli).

## Usage

Generate a new SAM based Serverless App: `sam init --location gh:coolblue-development/cookiecutter-dotnet-sam`.

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

## Options

Option | Description
------------------------------------------------- | ---------------------------------------------------------------------------------
`project_name` | Name of the project
`project_short_description` | A short description of the project, this will be used for the description of the AWS Stack and as part of the generated README.md file.
`project_app_group` | The AppGroup for deployment of the Lambda stack
`project_slug` | The name for the solution and main project
`use_kms` | Choose to add or not a shared adapter to allow decrypting values within your lambda.
`lambda_trigger_type` | You can choose between SQS and API, this will wire the lambda with a trigger of the selected type and setup the test tasks for local development
