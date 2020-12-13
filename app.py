#!/usr/bin/env python3

from aws_cdk import core

from cdk_pipelines_demo.cdk_pipelines_demo_stack import CdkPipelinesDemoStack


app = core.App()
CdkPipelinesDemoStack(app, "cdk-pipelines-demo")

app.synth()
