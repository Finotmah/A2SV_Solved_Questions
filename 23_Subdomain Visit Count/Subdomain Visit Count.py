class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_count = dict()

        for cpdomain in cpdomains:
            cpdomain = cpdomain.split()
            rep, domain = cpdomain
            if domain not in domain_count:
                domain_count[domain] = 0
            domain_count[domain] += int(rep)
            while "." in domain:
                index = domain.index(".")
                key = domain[index + 1:]
                if key not in domain_count:
                    domain_count[key] = 0
                domain_count[key] += int(rep)
                domain = key
        
        all_cpdomains = []

        for rep, domain in domain_count.items():
            all_cpdomains.append(str(domain) + " " + str(rep))
            
        return all_cpdomains
        
