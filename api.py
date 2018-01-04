from uuid import uuid4
from flask import Flask

from blockchain import Blockchain

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Init the Blockchain
blockchain = Blockchain()
