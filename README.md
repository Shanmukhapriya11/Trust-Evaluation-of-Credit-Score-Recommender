# SmartLoanChain: Trust-Evaluation of Credit Score Recommender Model Using Deep Learning and Blockchain

## Project Overview
This project introduces SmartLoanChain, a novel credit-recommender system leveraging deep learning and blockchain technology to facilitate secure, transparent, and efficient lending operations. It addresses the limitations of traditional credit rating agencies (CRAs) by providing a decentralized, transparent, and secure credit scoring and lending platform.

## Table of Contents
- Introduction
- System Model
- Methodology
- Performance Evaluation and Results
- Conclusion and Future Work
- Setup and Installation
- Usage
- Contributing

## Introduction
Traditional credit scoring methods often suffer from high costs, lack of transparency, and biases. SmartLoanChain addresses these issues by integrating blockchain technology with a Transformer-based deep learning model to predict credit scores and manage loans in a secure and transparent manner.

**Key features include:**
- **Blockchain Integration:** Secure storage of financial data with transparency and privacy.
- **Transformer Model:** Accurate prediction of credit scores using sequential financial data.
- **Smart Contracts:** Automated loan disbursement and repayment management.

## System Model

### Blockchain Integration
- Stores borrower’s historical financial data in a public blockchain with encryption and secure access.
- Utilizes a proof-of-stake consensus mechanism for efficiency and scalability.
- Employs decentralized identifiers (DIDs) and verifiable credentials (VCs) for authentication.

### Transformer Recommender Model
- Processes time-sequenced financial data stored in the blockchain.
- Uses self-attention mechanisms to capture complex relationships within the data.
- Generates real-time updates of credit scores with high accuracy.

## Methodology

### Data Collection and Preprocessing
- Financial data includes bank balances, loan histories, insurance details, and educational background.
- Preprocessing steps include normalization, encoding, and handling missing values.

### Model Training
- Trained on the Statlog UCI repository with 1000 credit histories.
- Achieved 86.4% accuracy with an F-measure of 0.84.
- Techniques such as cross-validation, regularization, and hyperparameter tuning were used.

### Smart Contracts
- Manages loan disbursement, repayment schedules, and collateral management.
- Written in Solidity and deployed on the Ethereum blockchain.

## Performance Evaluation and Results
- Achieved an accuracy of 86.4% with a high level of reliability and low computational costs.
- Demonstrated superior performance compared to traditional models such as logistic regression and decision trees.
- Continuous learning approach ensures adaptability to changing economic conditions.

## Conclusion and Future Work
SmartLoanChain provides a robust, transparent, and efficient solution for credit scoring and lending. Future work includes:
- Scaling the system for larger data volumes.
- Integrating additional data sources.
- Enhancing privacy and security through advanced cryptographic techniques.

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/SmartLoanChain.git
```

### Install Dependencies

**Install Python dependencies:**
```bash
pip install -r requirements.txt
```

**Install Node.js dependencies for the smart contract interface:**
```bash
npm install
```

### Blockchain Setup
- Deploy smart contracts to a local Ethereum network (e.g., Ganache).
- Update contract addresses in the configuration files.

### Model Training
```bash
python train_model.py
```

## Usage

### Start the Blockchain Node
```bash
ganache-cli
```

### Deploy Smart Contracts
```bash
truffle migrate --network development
```

### Run the Application
```bash
npm start
```

**Access the Application:**  
Open your browser and go to `http://localhost:3000` to access the SmartLoanChain interface.

## Contributing
We welcome contributions to improve SmartLoanChain! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.


For detailed methodology and architecture, see major_project_report
