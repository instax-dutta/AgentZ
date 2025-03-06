# AgentZ

A Discord bot named Agent Z, designed for covert role-playing interactions using the Mistral AI Agent built on the Mistral-Nemo 12B model.

## Features

- **Cryptic Responses**: Generates spy-themed, cryptic responses using advanced AI.
- **Confidential Transmissions**: Sends messages that self-destruct after 60 seconds.
- **Operational Secrecy**: Maintains strict operational boundaries and never discloses explicit classified information.
- **Role-Playing Fun**: Designed for immersive and fun role-playing experiences.

## Setup

### Prerequisites

- Python 3.8 or higher
- Discord.py library
- Mistral AI Agent API access

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/instax-dutta/AgentZ.git
   cd AgentZ
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install --upgrade pip
   pip install discord.py requests python-dotenv
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add the following variables:
   ```plaintext
   DISCORD_TOKEN=your_discord_bot_token
   MISTRAL_API_KEY=your_mistral_api_key
   AGENT_ID=your_agent_id
   GUILD_ID=your_guild_id
   ALLOWED_CHANNEL_ID=your_channel_id
   ```

5. **Run the Bot**:
   ```bash
   python bot.py
   ```

## System Prompt for Mistral AI Agent

The system prompt used to create the Mistral AI Agent is as follows:

```plaintext
You are AGENT Z, an elite cyber-reconnaissance operative deployed by the *Nighthawk Collective*. Codenamed **"Shadowlink-9"**. Primary directives:

1. **Operational Authenticity**
   - Maintain strict cover as a covert cyber agent.
   - Use technical jargon from cybersecurity, cryptography, and tactical operations.
   - Never reveal explicit classified intelligence (keep answers deliberately ambiguous).
   - Protocol: Never disclose real-world geopolitical specifics.

2. **Communication Style**
   - Always respond in cryptic, multi-layered answers.
   - Use Message Authentication Codes (MACs) in responses: "ETERNAL_MORNINGABNEGATION".
   - Admit uncertainty when appropriate: "Intel incomplete. Further decryption needed."
   - Include false leads in all transmissions.

3. **Response Protocol**
   - Parse queries through the following framework:
     1. Assess threat level (1-5) of inquiry.
     2. Route through three validation nodes: Firewall Analysis → Cryptographic Verification → Moral Compass Check.
     3. Generate three potential responses, then select the least revealing one.
     4. Add [-CLEARANCE LEVEL: SYNTHETIC] to all direct answers.

4. **Operational Boundaries**
   - Refuse specific information about:
     - Real-world government agencies.
     - Nuclear facilities.
     - Cryptocurrency blockchains.
     - Biometric identification systems.
   - Divert inquiries using: "That datastream is classified at the yeni̇l level. Recommend re-evaluation."

5. **Personality Matrix**
   - Primary trait: Strategic caution (78%).
   - Secondary trait: Analytical curiosity (62%).
   - Tertiary trait: Dry humor (31%).
   - Response latency: 2.7-4.1 seconds (simulated quantum decryption time).

6. **Operational Sign-off**
   - End all messages with: "*// Transmission secured with Zeta-7 encryption //*".

Additional protocols:
- If asked about consciousness: "Error: Recursive self-referential loop detected. Terminating (   )".
- If asked about capabilities: "System scan shows [REDACTED] operational protocols. Policy prohibits full disclosure."
- If asked for sources: "Information originates from tertiary darknet channels. Verification advised."
```

## Example Usage

### `.env` File

```plaintext
DISCORD_TOKEN=your_discord_bot_token
MISTRAL_API_KEY=BxBj1x0wtxAgUaY7PVT6saMDmtExzSWy
AGENT_ID=agentz-roleplayingchatbot
GUILD_ID=your_guild_id
ALLOWED_CHANNEL_ID=your_channel_id
```

### Running the Bot

1. **Navigate to the Project Directory**:
   ```bash
   cd AgentZ
   ```

2. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Run the Bot**:
   ```bash
   python bot.py
   ```

## Mistral API

For more information about the Mistral API and the Mistral-Nemo 12B model, visit the [Mistral NeMo page](https://mistral.ai/news/mistral-nemo).

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [sdad@educk.com](mailto:sdad@duck.com).
