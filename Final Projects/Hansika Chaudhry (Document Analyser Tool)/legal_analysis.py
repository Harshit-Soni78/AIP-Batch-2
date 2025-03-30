import re
from nltk.tokenize import sent_tokenize

# Dictionary of potentially problematic legal clauses
PROBLEMATIC_CLAUSES = {
    'unlimited_liability': [
        r'unlimit.*\s+liab.*',
        r'without\s+limit.*\s+liab.*',
        r'full.*\s+respons.*\s+for\s+all',
    ],
    'automatic_renewal': [
        r'automatic.*\s+renew',
        r'auto.*\s+extend',
        r'renew.*\s+unless\s+notif',
        r'continue\s+until\s+cancel',
    ],
    'unilateral_changes': [
        r'may\s+change\s+.*\s+at\s+(our|its)\s+discretion',
        r'reserve.*\s+right\s+to\s+modify',
        r'right\s+to\s+amend\s+.*\s+without\s+notice',
        r'sole\s+discretion',
    ],
    'arbitration': [
        r'mandatory\s+arbitration',
        r'binding\s+arbitration',
        r'waive\s+.*\s+right\s+to\s+sue',
        r'waive\s+.*\s+right\s+to\s+jury\s+trial',
    ],
    'class_action_waiver': [
        r'waive\s+.*\s+class\s+action',
        r'no\s+class\s+arbitration',
        r'individual\s+capacity\s+only',
        r'not\s+as\s+.*\s+class\s+representative',
    ],
    'exclusion_liability': [
        r'not\s+liable\s+for',
        r'no\s+liability\s+for',
        r'disclaim.*\s+all\s+liab.*',
        r'shall\s+not\s+be\s+held\s+responsible',
    ],
    'termination_without_cause': [
        r'terminat.*\s+at\s+any\s+time',
        r'discontinue\s+.*\s+for\s+any\s+reason',
        r'terminat.*\s+without\s+cause',
        r'right\s+to\s+cancel\s+.*\s+at\s+(our|its)\s+discretion',
    ],
    'data_use': [
        r'use\s+your\s+data\s+for',
        r'collect\s+.*\s+information',
        r'share\s+.*\s+with\s+third\s+part',
        r'sell\s+.*\s+information',
    ],
    'indemnification': [
        r'indemnif',
        r'hold\s+harmless',
        r'defend\s+.*\s+against\s+any\s+claim',
    ],
    'jurisdiction': [
        r'govern.*\s+by\s+the\s+laws\s+of',
        r'venue\s+.*\s+shall\s+be',
        r'exclusive\s+jurisdiction',
    ],
    'hidden_fees': [
        r'additional\s+fee',
        r'processing\s+fee',
        r'service\s+charge',
        r'subject\s+to\s+.*\s+fee',
    ]
}

def detect_hidden_clauses(text):
    """Detect potentially hidden or unfair clauses in legal contracts."""
    sentences = sent_tokenize(text)
    
    results = {}
    for clause_type, patterns in PROBLEMATIC_CLAUSES.items():
        matching_sentences = []
        
        for sentence in sentences:
            lower_sent = sentence.lower()
            for pattern in patterns:
                if re.search(pattern, lower_sent):
                    matching_sentences.append(sentence.strip())
                    break
        
        if matching_sentences:
            results[clause_type] = matching_sentences
    
    # Generate report
    report = []
    report.append("HIDDEN CLAUSE DETECTION REPORT\n")
    
    if not results:
        report.append("No potentially problematic clauses detected.")
    else:
        report.append(f"Found potentially problematic clauses in {len(results)} categories:\n")
        
        for clause_type, sentences in results.items():
            # Convert clause_type from snake_case to Title Case
            clause_name = ' '.join(word.capitalize() for word in clause_type.split('_'))
            
            report.append(f"\n** {clause_name} Clauses **")
            report.append("Description: " + get_clause_description(clause_type))
            report.append("Risk Level: " + get_risk_level(clause_type))
            report.append("Detected instances:")
            
            for i, sentence in enumerate(sentences[:5], 1):
                report.append(f"  {i}. {sentence}")
            
            if len(sentences) > 5:
                report.append(f"  ...and {len(sentences) - 5} more instances.")
    
    return "\n".join(report)

def get_clause_description(clause_type):
    """Get description for a clause type."""
    descriptions = {
        'unlimited_liability': "Clauses that make you responsible without financial limits for damages or losses.",
        'automatic_renewal': "Contract automatically renews without explicit consent or notification.",
        'unilateral_changes': "Allows the other party to change terms without your approval or notice.",
        'arbitration': "Forces disputes into private arbitration instead of court, often favorable to businesses.",
        'class_action_waiver': "Prevents you from joining class action lawsuits against the company.",
        'exclusion_liability': "Company disclaims responsibility for damages, even if caused by their negligence.",
        'termination_without_cause': "Allows the other party to end the agreement for any or no reason.",
        'data_use': "Permits broad use, sharing, or selling of your personal information.",
        'indemnification': "You must defend and pay for legal issues involving the other party.",
        'jurisdiction': "Forces legal disputes to be handled in a location favorable to the other party.",
        'hidden_fees': "Allows for additional charges that aren't clearly disclosed upfront."
    }
    return descriptions.get(clause_type, "Potentially problematic legal clause")

def get_risk_level(clause_type):
    """Determine risk level of a clause type."""
    high_risk = ['unlimited_liability', 'class_action_waiver', 'indemnification']
    medium_risk = ['unilateral_changes', 'arbitration', 'exclusion_liability', 'termination_without_cause']
    
    if clause_type in high_risk:
        return "HIGH"
    elif clause_type in medium_risk:
        return "MEDIUM"
    else:
        return "LOW"
