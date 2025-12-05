# AgentLend 
🏦 AgentLend – AI-Driven Loan Assistance Platform

AgentLend is a smart Agentic AI lending system that automates end-to-end loan processing for NBFCs.
It uses a Master Agent and multiple Worker Agents to handle:

Loan conversation

KYC verification

Credit evaluation

EMI visualization

Fairness & explainability

Sanction letter generation

Built with FastAPI, React, LangFlow, Groq LLM, MongoDB Atlas, and MySQL.

🚀 Tech Stack
Frontend

React

Vite

Recharts (EMI visualization)

Backend

FastAPI

LangFlow (Agent Orchestration)

Groq LLM

JWT Authentication (later)

Databases

MongoDB Atlas (CRM / Customer KYC data)

MySQL (Loan limits, interest rates, underwriting rules)

Other Tools

ReportLab (PDF generation)

Python-dotenv

Uvicorn

🤖 Agent Architecture
Master Agent

Controls full conversation flow

Calls worker agents based on state

Ensures the complete loan pipeline runs smoothly

Worker Agents

Sales Agent – collects loan details

Verification Agent – checks KYC using MongoDB

Underwriting Agent – evaluates eligibility using MySQL

Fair Check Agent – generates unbiased decision explanations

EMI View Agent – calculates EMI & visualizes

Loan Guide Agent – suggests alternate offers

Sanction Agent – generates sanction letter PDF
