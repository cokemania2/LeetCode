class Solution:
    def format_number_with_dot(self, number: int) -> str:
        # 쉼표로 구분된 문자열로 변환
        number_str = f"{number:,}"
        # 쉼표를 점으로 변환
        return number_str.replace(",", ".")

    def thousandSeparator(self, n: int) -> str:
        return self.format_number_with_dot(n)
