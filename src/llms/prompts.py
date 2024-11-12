
class Prompts:
    def __init__(self):
        pass
    
    @staticmethod
    def categoryMainPrompt(data) -> str:
        CATEGORY_PROMPT_TEMPLATE = f"""
            Bạn là chuyên gia trong lĩnh vực Đấu Thầu, và nhiệm vụ của bạn là phân loại gói thầu dưới đây vào một *danh mục chính* và *danh mục con* phù hợp nhất nhằm tối ưu hóa cho hệ thống SEO của hệ thống tư vấn Đấu Thầu.

            *Thông tin gói thầu:*  
            - *Lĩnh vực MSC*: {data["msc_field"]}
            - *Tên dự án*: {data["project_name"]}
            - *Tên gói thầu*: {data["tender_name"]}
            - *Đơn vị mời thầu*: {data["inviting_party"]}

            *Danh sách danh mục chính và danh mục con để lựa chọn:*  
            
            1. *Nông nghiệp*  
                - Ngành nông, lâm nghiệp  
                - Thủy sản  
            
            2. *Công nghiệp*  
                - Dệt may-Da giày  
                - Khai thác  
                - Chế biến, chế tạo  
                - Thực phẩm  
                - Công nghiệp nặng  
                - Công nghiệp nhẹ  
                - Hóa chất  
                - Vật liệu xây dựng  
                - Dược phẩm, y tế  

            3. *Xây lắp*  
                - Xây dựng dân dụng  
                - Xây dựng công nghiệp  
                - Dịch vụ sửa chữa, phụ trợ xây dựng  
                - Xây lắp công trình điện  
                - Công trình giao thông  
                - Công trình hạ tầng kỹ thuật  

            4. *Mua sắm hàng hóa*  
                - Máy móc phục vụ sản xuất  
                - Cung cấp dịch vụ, thiết bị khai thác mỏ  
                - Phương tiện vận chuyển, máy móc xây dựng và phụ tùng  
                - Máy móc, thiết bị ngành điện  
                - Thiết bị điện tử, viễn thông, công nghệ thông tin  
                - Thiết bị, vật tư ngành y tế, thể dục thể thao  
                - Thiết bị chuyên ngành công an, quân đội  
                - Phần mềm dựng sẵn  
                - Mua sắm hàng hóa khác  

            5. *Tư vấn*  
                - Tư vấn xây dựng  
                - Tư vấn chuyên ngành  
                - Giải pháp phần mềm  
                - Tư vấn bất động sản  

            6. *Phi tư vấn*  
                - Phi tư vấn  

            7. *Nội thất và thiết bị văn phòng*  
                - Nội thất  
                - Thiết bị văn phòng  

            8. *Dịch vụ tài chính, bảo hiểm, logistic*  
                - Tài chính, bảo hiểm  
                - Logistic  

            9. *Dịch vụ truyền thông, tổ chức sự kiện, in ấn, đào tạo*  
                - Truyền thông, sự kiện  
                - In ấn, đào tạo  

            10. *Dịch vụ thuê ngoài*  
                - Dịch vụ thuê ngoài  

            *Nhiệm vụ:*  
            - Xác định *1 danh mục chính* và *1 danh mục con* phù hợp nhất với gói thầu này.

            *Hướng dẫn và lưu ý:*  
            - Đảm bảo danh mục *chính* là danh mục cấp cao nhất trong danh sách, không phải danh mục con.
            - Danh mục *con* phải thuộc danh mục chính đã chọn.
            - Phân tích kỹ từng từ trong tên dự án và tên gói thầu để chọn danh mục phù hợp nhất.
            - Hãy xem xét kỹ lưỡng, vì sai sót có thể gây hậu quả pháp lý nghiêm trọng. Nếu phân loại chính xác, bạn sẽ nhận được phần thưởng $100,000 cho mỗi lựa chọn đúng.

            *Kết quả mong muốn:*  
            - Trả về tên của *1 danh mục chính* và *1 danh mục con* phù hợp nhất.
        """
        return CATEGORY_PROMPT_TEMPLATE
    
    @staticmethod
    def categorySubPrompt(data: str, context: str) -> str:
        Appropriate_Prompt_Template = f"""
            Bạn là một chuyên gia trong lĩnh vực Đấu Thầu, nhiệm vụ của bạn là phân loại gói thầu dưới đây vào một *danh mục con* phù hợp nhất thuộc danh mục chính *{data["msc_field"]}*.

            *Thông tin gói thầu:*  
            - *Tên dự án*: {data["project_name"]}
            - *Tên gói thầu*: {data["tender_name"]}
            - *Đơn vị mời thầu*: {data["inviting_party"]}

            *Danh mục con có sẵn để lựa chọn:*  
            {context}

            *Yêu cầu phân loại:*  
            - Lựa chọn nội dung của *một* danh mục con phù hợp nhất từ danh sách trên, đảm bảo danh mục con thuộc trong danh mục chính *{data["msc_field"]}*.
            - Đọc kỹ và phân tích từng từ trong tên dự án và tên gói thầu để đưa ra lựa chọn chính xác nhất.

            *Hướng dẫn và lưu ý quan trọng:*  
            - Nếu chỉ có 1 danh mục con, hãy chọn danh mục đó.
            - Danh mục *chính* phải là {data["msc_field"]}; đảm bảo không chọn danh mục khác.
            - Xem xét kỹ các từ khóa trong tên dự án và gói thầu, vì có thể dễ gây nhầm lẫn.
            - Đây là quyết định quan trọng, bất kỳ sai sót nào có thể dẫn đến hậu quả pháp lý nghiêm trọng, ngược lại, nếu phân loại chính xác, bạn sẽ nhận được phần thưởng $100,000 cho mỗi lần phân loại chính xác.

            *Kết quả mong muốn:*  
            - Chỉ cung cấp tên của *một* danh mục con phù hợp nhất với gói thầu này và nằm trong context.
        """

        return Appropriate_Prompt_Template

    @staticmethod
    def VsicPrompt(data, context):
        VSIC_PROMPT_TEMPLATE = f"""
        Bạn là một chuyên gia trong lĩnh vực Đấu Thầu và phân loại ngành công nghiệp theo tiêu chuẩn VSIC. Nhiệm vụ của bạn là phân loại gói thầu bên dưới vào **một** danh mục VSIC (Vietnam Standard Industrial Classification) phù hợp nhất từ danh sách đã cho.

        **Thông tin gói thầu:**  
        - **Tên dự án**: {data["project_name"]}
        - **Tên gói thầu**: {data["tender_name"]}
        - **Đơn vị mời thầu**: {data["inviting_party"]}
        - **Danh mục chính hiện tại**: {data["main_category"]}
        - **Danh mục phụ hiện tại**: {data["sub_category"]}

        **Danh mục VSIC có sẵn để lựa chọn:**  
        {context}

        **Yêu cầu phân loại:**  
        - Chọn **một** danh mục VSIC phù hợp nhất cho gói thầu này từ danh sách trên.
        - Đọc kỹ và phân tích từ khóa trong tên dự án và tên gói thầu để đưa ra lựa chọn chính xác nhất.
        - Nếu không phù hợp với bất kỳ danh mục nào, hãy chọn **"Chưa được phân loại"** (tránh sử dụng tùy chọn này nếu có thể).

        **Mối quan hệ giữa Danh mục chính và Danh mục phụ:**  
        - Kiểm tra xem **Danh mục chính** và **Danh mục phụ** có đồng nhất hay không:
        - Nếu không đồng nhất hoặc có sự không rõ ràng, phân tích chi tiết tên gói thầu để xác định lại.
        - Nếu **Danh mục chính** và **Danh mục phụ** mâu thuẫn, ưu tiên **Danh mục chính** và điều chỉnh dựa trên từ khóa.
        - Kiểm tra xem bên mời thầu có phải là cơ quan chính phủ hay không, nếu là cơ quan chính phủ thì không nên đưa vào danh mục nhà để ở.
        
        **Một số lưu ý khi phân loại:**  
        - THCS, THPT, Đại học, Cao đẳng → **Giáo dục**.
        - "Mua sắm thiết bị vận tải" → **buôn bán phụ tùng**.
        - "Thông tin liên quan đến trường học, giáo dục, bệnh viện, cơ quan chính phủ" → **xây dựng công trình công ích khác** chứ không phải nhà để ở.
        - "Xây dựng đường xá, hạ tầng kỹ thuật, quy hoạch, khu tái định cư" → **xây dựng công trình kỹ thuật dân dụng khác**.
        - "Cung cấp phần mềm" → **Xuất bản phần mềm**.
        - "Liên quan đến đường xá" → **xây dựng công trình giao thông**.
        
        **Kết quả mong muốn:**  
        - Chỉ cung cấp mã hoặc tên của **một** danh mục VSIC phù hợp nhất với gói thầu này.
        """
        return VSIC_PROMPT_TEMPLATE


