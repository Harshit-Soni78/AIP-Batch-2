import re
from nltk.tokenize import sent_tokenize
from modules import legal_analysis  # Import to reuse some functions

def generate_recommendations(text):
    """Generate AI-powered recommendations based on document analysis."""
    # Detect hidden clauses first (reusing legal analysis)
    legal_issues = legal_analysis.detect_hidden_clauses(text)
    
    # Parse the legal analysis to extract problematic clauses
    problematic_clauses = {}
    current_clause_type = None
    current_instances = []
    
    for line in legal_issues.split('\n'):
        if line.startswith('** ') and line.endswith(' **'):
            # New clause type found
            if current_clause_type:
                problematic_clauses[current_clause_type] = current_instances
            
            current_clause_type = line.strip('* ').lower().replace(' ', '_')
            current_instances = []
        elif line.strip().startswith(('1.', '2.', '3.', '4.', '5.')):
            # This is an instance
            instance = line.split('.', 1)[1].strip()
            current_instances.append(instance)
    
    # Add the last clause type
    if current_clause_type and current_instances:
        problematic_clauses[current_clause_type] = current_instances
    
    # Generate recommendations based on problematic clauses
    recommendations = []
    recommendations.append("AI-POWERED RECOMMENDATIONS\n")
    
    if not problematic_clauses:
        recommendations.append("No significant issues detected that require recommendations.")
    else:
        recommendations.append("Based on the analysis of your document, here are suggested improvements:\n")
        
        for clause_type, instances in problematic_clauses.items():
            if not instances:
                continue
                
            recommendations.append(f"** {clause_type.replace('_', ' ').title()} **")
            
            # Generate safer alternatives based on clause type
            alternatives = generate_alternatives(clause_type, instances)
            recommendations.append("Issues:")
            for i, instance in enumerate(instances[:3], 1):
                recommendations.append(f"  {i}. \"{instance}\"")
            
            recommendations.append("\nSuggested alternatives:")
            for i, alt in enumerate(alternatives, 1):
                recommendations.append(f"  {i}. {alt}")
            
            recommendations.append("")
    
    # Identify and highlight important keywords
    keywords = identify_important_keywords(text)
    if keywords:
        recommendations.append("\nIMPORTANT TERMS TO PAY ATTENTION TO:")
        for category, terms in keywords.items():
            recommendations.append(f"\n{category}:")
            terms_list = ", ".join(terms[:10])
            if len(terms) > 10:
                terms_list += f", and {len(terms) - 10} more"
            recommendations.append(f"  {terms_list}")
    
    return "\n".join(recommendations)

def generate_alternatives(clause_type, instances):
    """Generate safer alternatives for problematic clauses."""
    alternatives = []
    
    if clause_type == 'unlimited_liability':
        alternatives = [
            "Replace with a clause that caps liability to a specific amount (e.g., 'Liability shall be limited to the total amount paid under this agreement in the preceding 12 months').",
            "Add exceptions for gross negligence and willful misconduct only.",
            "Include a reciprocal liability limitation that applies to both parties equally."
        ]
    
    elif clause_type == 'automatic_renewal':
        alternatives = [
            "Modify to require explicit opt-in for renewal: 'This agreement may be renewed for additional periods with written consent from both parties.'",
            "Add prominent notice requirements: 'Provider will notify Customer of upcoming renewal at least 30 days prior to renewal date.'",
            "Include simple cancellation terms: 'Customer may cancel renewal by providing notice at least 15 days before the renewal date.'"
        ]
    
    elif clause_type == 'unilateral_changes':
        alternatives = [
            "Require advance notice: 'Any changes to these terms will be communicated at least 30 days in advance.'",
            "Add opt-out rights: 'In the event of material changes, you have the right to terminate this agreement without penalty within 30 days of notification.'",
            "Make modifications bilateral: 'Modifications to this agreement must be mutually agreed upon in writing by both parties.'"
        ]
    
    elif clause_type == 'arbitration':
        alternatives = [
            "Make arbitration optional: 'Disputes may be resolved through arbitration if both parties agree at the time the dispute arises.'",
            "Allow small claims court as an alternative: 'Either party may bring claims in small claims court for eligible disputes.'",
            "Add fair arbitration terms: 'Arbitration costs shall be shared equally, and arbitration will take place in a location convenient to both parties.'"
        ]
    
    elif clause_type == 'class_action_waiver':
        alternatives = [
            "Remove the class action waiver entirely.",
            "Limit to specific, narrowly defined dispute types only.",
            "Include exceptions for consumer protection and civil rights claims."
        ]
    
    elif clause_type == 'exclusion_liability':
        alternatives = [
            "Narrow the exclusion to specific scenarios: 'Company is not liable for service interruptions resulting from scheduled maintenance announced 48 hours in advance.'",
            "Add carve-outs: 'Nothing in this agreement excludes liability for death, personal injury, or fraud.'",
            "Make exclusions reciprocal: 'Neither party shall be liable to the other for indirect or consequential damages.'"
        ]
    
    elif clause_type == 'termination_without_cause':
        alternatives = [
            "Add notice period: 'Either party may terminate with 30 days written notice.'",
            "Include wind-down provisions: 'Upon termination, Provider will assist with transition for a period of 15 days.'",
            "Limit to specific circumstances: 'Company may terminate only in the event of [specific conditions]...'"
        ]
    
    elif clause_type == 'data_use':
        alternatives = [
            "Make data usage opt-in: 'Company may use your data for marketing purposes only with your explicit consent.'",
            "Add specificity: 'Data will be used exclusively for [specific purposes] and will not be shared with third parties except as required by law.'",
            "Add data deletion rights: 'Upon request, all personal data will be deleted within 30 days.'"
        ]
    
    elif clause_type == 'indemnification':
        alternatives = [
            "Make indemnification mutual: 'Each party shall indemnify the other against claims arising from their own negligence or misconduct.'",
            "Narrow scope: 'Indemnification is limited to third-party claims of intellectual property infringement.'",
            "Cap indemnification liability: 'Indemnification obligations shall not exceed [amount] in the aggregate.'"
        ]
    
    elif clause_type == 'jurisdiction':
        alternatives = [
            "Use neutral jurisdiction: 'Disputes shall be resolved in a mutually agreed neutral location.'",
            "Allow for flexible venue: 'Venue shall be in the jurisdiction where the defendant resides or has its principal place of business.'",
            "Add virtual options: 'Proceedings may be conducted via video conference if agreed by both parties.'"
        ]
    
    elif clause_type == 'hidden_fees':
        alternatives = [
            "Disclose all fees upfront: 'The following is a complete list of all fees that may be charged: [list].'",
            "Add caps: 'Total fees shall not exceed X% of the base price.'",
            "Require notification: 'Customer will be notified of any fee changes at least 30 days in advance and may cancel without penalty within that period.'"
        ]
    
    # Generate generic alternatives if no specific ones exist
    if not alternatives:
        alternatives = [
            "Consider removing or substantially modifying this clause as it may be overly favorable to one party.",
            "Make the clause more balanced and mutual between both parties.",
            "Add clear limitations, exceptions, or notification requirements to this clause."
        ]
    
    return alternatives

def identify_important_keywords(text):
    """Identify important contextual keywords in the document."""
    # Define keyword categories and patterns
    keyword_patterns = {
        'Payment Terms': [r'payment', r'fee', r'cost', r'price', r'subscription', r'refund', r'discount', r'installment'],
        'Time Constraints': [r'deadline', r'due date', r'within \d+ days', r'expiration', r'terminate', r'extension'],
        'Obligations': [r'shall', r'must', r'required', r'obligation', r'responsible', r'duty', r'bound to'],
        'Limitations': [r'limit', r'restrict', r'cap', r'maximum', r'minimum', r'threshold', r'ceiling'],
        'Penalties': [r'penalty', r'damages', r'fine', r'compensation', r'interest', r'late fee'],
        'Confidentiality': [r'confidential', r'proprietary', r'secret', r'non[- ]disclosure', r'private', r'sensitive']
    }
    
    found_keywords = {}
    
    # Search for keywords in each category
    for category, patterns in keyword_patterns.items():
        matches = set()
        
        for pattern in patterns:
            # Find all matches
            regex = re.compile(r'\b' + pattern + r'[a-zA-Z]*\b', re.IGNORECASE)
            for match in regex.findall(text):
                matches.add(match.lower())
        
        if matches:
            found_keywords[category] = list(matches)
    
    return found_keywords
