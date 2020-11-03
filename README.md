# Azure Machine Learning Gallery

Azure Machine Learning Gallery enables our growing community of developers and data scientists to share their machine learning pipelines, components, etc. to accelerate productivity in the machine learning lifecycle.

In this gallery, you can easily find a machine learning pipeline/component which is similar to the problem you are trying to solve, rather than starting from scratch.

## What is pipeline and component 

An Azure Machine Learning pipeline is an independently executable workflow of a complete machine learning task. Azure Machine Learning pipelines help you build, optimize, and manage machine learning workflows with simplicity, repeatability and quality assurance.


A component is self-contained set of code that performs one step in the ML workflow (pipeline), such as data preprocessing, model training, model scoring and so on. A component is analogous to a function, in that it has a name, parameters, expects certain input and returns some value. 

 
Data scientists or developers can wrap their arbitrary code as Azure Machine Learning component by following the component specification.

### Component specification

A component specification in YAML format describes the component in the Azure Machine Learning system. A component definition has the following parts:

- **Metadata:** name, description, etc.
- **Interface:**: input/output specifications (name, type, description, default value, etc).
- **Implementation:**: A specification of how to run the component given a set of argument values for the component’s inputs, including source code and environment required to run the component. 

Refer to [component spec definition](./component-spec-definition.md) for more details. 



## Quick Links
* [Pipelines list](/pipelines/README.md) - highlights of end to end machine learning workflows in multipe domains like text analytics, computer vision, recommendation, etc.
* [Components list](/components/README.md) - a catalog of components which can be reused in different pipelines


## Tutorial
- [Tutorial 1: Use existing component from gallery](./tutorial/tutorial1-use-existing-components.md)
- Toturial 2: Create your own component
## Get Involved
Please email us: stcamlstudio@microsoft.com

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.

# Containerization Preview Terms of Use

These terms of use apply only to the containerization preview.

This preview is made available to you on the condition that you agree to the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/) which supplement [your agreement](https://azure.microsoft.com/en-us/support/legal/) governing use of Azure.

The preview, including its user interface, features and documentation is confidential and proprietary to Microsoft and its suppliers. For five (5) years after access of this service or its commercial release, whichever is first, you may not disclose confidential information to third parties. You may disclose confidential information only to your employees and consultants who need to know the information. You must have written agreements with them that protect the confidential information at least as much as these terms. Your duty to protect confidential information survives these terms.

You may disclose confidential information in response to a judicial or governmental order. You must first give written notice to Microsoft to allow it to seek a protective order or otherwise protect the information. Confidential information does not include information that (i) becomes publicly known through no wrongful act; (ii) you received from a third party who did not breach confidentiality obligations to Microsoft or its suppliers; or (iii) you developed independently.

If you give feedback about the preview to Microsoft, you give to Microsoft, without charge, the right to use, share and commercialize your feedback in any way and for any purpose. You will not give feedback that is subject to a license that requires Microsoft to license its software or documentation to third parties because Microsoft includes your feedback in them. These rights survive these terms.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

<a href="https://trackgit.com"><img src="https://sfy.cx/u/oAu" alt="trackgit-views" /></a> _views_