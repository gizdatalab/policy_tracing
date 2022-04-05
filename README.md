<p align="right">
  <img width="200" src="https://github.com/gizdatalab/policy_tracing/blob/main/img/sdsn.png" alt="sdsn">
</p> 
    
# Tracing Policy Implementations 2.0
This repo scals the ideas of the ETH Hack4Good Hachathon 2021 with SDSN & GIZ  
https://www.blog-datalab.com/policy-tracing-nlp-h4g

<p align="center">
  <img width="600" src="https://github.com/gizdatalab/policy_tracing/blob/main/img/ndc_policy.png" alt="policy">
</p>

# The Problem
Worlds main problem is the progressing climate change and too few efforts to stop it. The 26th UN Climate Change Conference of the Parties (COP26) in 2021 was filled with promises of governmental action to help tackle climate change. The national adaptation and mitigation goals are laid down in the nationally determined contribution
(NDC).   
Example NDC from South Africa: [NDC South Africa](https://www.dffe.gov.za/sites/default/files/docs/southafricasINDCupdated2021sept.pdf)  
Excample Policy Document: [National REDD SA](https://www.researchgate.net/publication/236347801_South_Africa's_national_REDD_initiative_Assessing_the_potential_of_the_forestry_sector_on_climate_change_mitigation)

# Project Goal
The goal of the policy implementation tracing is to help Ppolicy advisors to connect the national NDCs with policy documents to check if the goals are realised.
We therefore build a web-application where polica analysts can upload a policy document which then gets analyzed for:  

## 1) Overall Topic of the documents (Summary)  
  * TF-IDF /   Text suammarization  
  * 
<p align="center">
  <img width="400" src="https://github.com/gizdatalab/policy_tracing/blob/main/img/topics.png" alt="topics">
</p>
  
## 2) Sustainable Development Goals related topics
  * Classification using Transformer and data from https://osdg.ai/ 
  
## 3) NDC related topics 
  * Using keyword ontologies and semantic search  

<p align="center">
  <img width="400" src="https://github.com/gizdatalab/policy_tracing/blob/main/img/semantic_search.png" alt="semantic_search">
</p>

## 4) Coherence to national NDC
  * compare policy to NDC document 
  
    
Open Questions:
  * Processing only machine readable PDF and Docx
  * how to split long documents
  * Summarization possible with OS ressources (Transformer; runtime, usage limits)
  * Topic modelling on NDCs?
  * Named Entity Recognition?
  * SDG classification with OS ressources (Transformer; runtime, usage limits)
  * vector search with OS ressources (Transformer; runtime, usage limits)
  * Coherence measurement BLEU score vs. text similarity vs. ...
  * Streamlit vs. Gradio (Spaces)
  * Adapting model to domain
  * Multiligunal models vs translation
  * Deployment of Azure Cloud ressources
  * Carbon Footprint
  * Transparency on transformer model (training data)

Streamlit Demo:  
https://share.streamlit.io/janmuehlnikel/streamlit_demo/app.py

