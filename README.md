# SmartLoanChain: Trust-Evaluation of Credit Score Recommender Model Using Deep Learning and Blockchain

## Project Overview
SmartLoanChain is an innovative credit-recommender system designed to facilitate secure, transparent, and efficient lending operations between borrowers and lenders. It leverages a Transformer-based deep learning model to evaluate financial trust and predict credit scores, eliminating the dependency on traditional credit rating agencies (CRAs). This AI-first system provides real-time updates of credit scores and integrates secure data management practices, with optional blockchain enhancements for future scalability.

## Table of Contents
- Introduction
- System Architecture
- Transformer Model
- Methodology
- Performance Evaluation
- Conclusion and Future Work
- Setup and Installation
- Usage
- Contributing

## Introduction
Traditional CRAs suffer from high costs, opacity, and bias. SmartLoanChain addresses these by integrating a Transformer model capable of handling sequential financial data to provide fair, accurate, and real-time credit evaluations. Financial data includes income, loan histories, insurance, and more, enriched by encryption and secure access protocols.

## System Architecture

### Secure Financial Data Management
- Financial attributes: bank assets, tax records, insurance, education.
- Security layers: hashing, AES encryption, public-private key authentication.
- Identity protection: uses Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs).
- Integration with external financial systems for real-time compatibility.

## Transformer Model: AI Engine of SmartLoanChain

- **Architecture**: Encoder-decoder model with self-attention mechanisms.
- **Data Processed**: Time-ordered sequences of user financial behavior.
- **Output**: A comprehensive and explainable credit score.
- **Features**: High interpretability with attention maps, fast real-time processing, supports continuous learning.

## Methodology

### Data Preprocessing
- **Normalization**: MinMaxScaler for uniform scale.
- **Encoding**: LabelEncoder for categorical data.
- **Imputation**: SimpleImputer to handle missing values.

### Model Training
- Dataset: 5000 samples from UCI Statlog (4500 positive, 500 default).
- Train-Test Split: 90:10
- Metrics: Accuracy = 97.01%, F1 Score = 0.97, Precision = 0.98, Recall = 0.96.
- Optimization: Cross-validation, dropout regularization, L2, and hyperparameter tuning.
- Augmentation: Noise injection, synthetic mixing, sequence variation.
- Learning Strategy: Continuous learning with routine model updates.

## Performance Evaluation
- Confusion Matrix shows superior classification capability.
- ROC and AUC confirm strong predictive performance.
- Compared with ANN-LSTM (KiRTi) and other deep learning/ensemble methods; Transformer outperforms across metrics.

## Conclusion and Future Work
SmartLoanChain redefines credit scoring with deep learning precision and secure data design. Future enhancements will include:
- Distributed computing for real-time scalability.
- Integration of alternative data sources (e.g., digital payments, housing, education).
- Zero-knowledge proofs and homomorphic encryption for enhanced privacy.

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/SmartLoanChain.git
```

### Install Dependencies
```bash
pip install -r requirements.txt
npm install
```

### Blockchain Setup (Optional for future integration)
- Use Ganache for local Ethereum network
- Deploy with Truffle
- Update smart contract addresses

### Model Training
```bash
python train_model.py
```

## Usage

### Start Blockchain Node
```bash
ganache-cli
```

### Deploy Contracts (if enabled)
```bash
truffle migrate --network development
```

### Run Application
```bash
npm start
```

Then access it via: `http://localhost:3000`

## Contributing
We welcome contributions to improve SmartLoanChain:
1. Fork the repository
2. Create a feature branch
3. Submit a detailed pull request

