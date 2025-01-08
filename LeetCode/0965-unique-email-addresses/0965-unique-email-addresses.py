class Solution:
    def filterEmails(self, email: str) -> str:
        local_name, domain_name = email.split('@')
        plus_filtered = local_name.split('+')[0]
        dot_filtered = ''.join(plus_filtered.split('.'))
        return dot_filtered + '@' + domain_name
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            email_set.add(self.filterEmails(email))
        return len(email_set)