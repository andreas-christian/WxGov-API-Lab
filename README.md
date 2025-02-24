# WxGov-API-Lab

The **Governance Console** (a.k.a. OpenPages) of **IBM Watsonx.governance** provides a **REST API** and a **Java API**. This workshop provides a hands-on overview of these APIs and explains how they can be used to interact with external systems.

For example, an external system may need to create objects like “models” and “use cases” in the Governance Console and prepopulate them with data.
A workflow in the Governance Console may need to trigger tasks in external systems, for example, creating a support ticket or triggering the deployment of an ML model.
This lab is the outcome of a project with one of the largest banks in Germany. It explains some of the bank’s requirements and how these requirements can be fulfilled with the APIs available in Watsonx.governance. 

The lab is divided into two parts:
* Part 1: An introduction to the REST API which explains how to retrieve, create and update model risk governance (MRG) objects in the Governance Console.
* Part 2: An introduction to the Java API that explains how to create a custom workflow action. We will use a custom workflow action that can execute REST calls to external systems. Optionally, you can customize this action to execute your own REST functions.
To complete part 1 of the workshop you need access to an IBM Cloud Pak for Data system with watsonx.governance (Factsheets, OpenPages, OpenScale) and Watson Studio enabled. This system may be a dedicated system or a shared system.

To complete part 2 of the workshop you need admin access to the Cloud Pak for Data system and you need to deploy an additional side-car VM. The VM is used to compile the custom workflow action (Java code) and it contains a REST server that Watsonx.governance will interact with.

Please check the lab guide (**Watsonx.gov-API-Lab-Description.pdf**) in the Git repository for a detailed description of the lab exercises and how to reserve the required lab environment.
