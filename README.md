# Sprint 4: API Testing Project  

## Project Overview  
This project focuses on testing new functionalities in the API of **Urban.Grocers**, as part of the back-end development update. The task includes analyzing requirements, designing test cases, and validating API endpoints for two core features: managing kits and checking delivery service availability.  

---

## Objectives  

1. **Analyze Requirements**:  
   - Review the back-end requirements and API documentation in apiDoc for new features.  
   - Focus on endpoints related to kits and delivery services.  

2. **Design Test Cases**:  
   - Create a checklist of tests to ensure the functionality works as expected.  
   - Document the checklist in Google Sheets and make it shareable with comment access.  

3. **API Testing with Postman**:  
   - Validate API responses for each endpoint.  
   - Submit bug reports in Jira for any issues identified.  

4. **Optional**:  
   - Compile a test report summarizing findings and the state of the tested product.  

---

## New Features to Test  

### **1. Kit Management**  
- Endpoint: `POST /api/v1/kits/{id}/products`  
- **Description**: Adds groceries to a kit.  
- **Validation**: The endpoint should return a `400 Bad Request` when the total number of unique products in a kit exceeds 30.  

### **2. Delivery Services**  
- Endpoint: `POST /order-and-go/v1/delivery`  
- **Description**: Checks if the Order and Go delivery service is available and calculates its cost.  
- **Validation**: Follow the pricing calculation rules and validate responses for service availability and cost.  

---

## Steps  

1. **Analyze Documentation**:  
   - Study the API documentation in apiDoc under "Main.Kits" and "Couriers" sections.  
   - Understand the requirements for the endpoints mentioned above.  

2. **Create a Checklist**:  
   - Use a Google Sheets template to document test scenarios for the new features.  
   - Ensure each test case is labeled as **PASSED** or **FAILED** after execution.  

3. **Test with Postman**:  
   - Use Postman to send requests to the API endpoints and validate their responses.  
   - For failed cases, create detailed bug reports in Jira and include links to the reports in the checklist.  

4. **Share Your Work**:  
   - Provide commenting access to the checklist using Google Sheets’ sharing settings.  
   - Submit the link to the platform for review.  

---

## Deliverables  

1. **Checklist**: A comprehensive Google Sheet covering all test cases.  
2. **Bug Reports**: Jira tickets documenting any identified issues.  
3. **Optional Test Report**: A summary of the tests conducted, findings, and product status.  

---

## Tools and Resources  

- **Postman**: For API testing and validation.  
- **Google Sheets**: To document the test checklist.  
- **Jira**: For bug reporting.  
- **apiDoc**: API documentation reference.  

---

## Evaluation Criteria  

1. Test cases are well-structured and address the given requirements.  
2. Tests are executed thoroughly, and results are accurately documented.  
3. Bugs are correctly identified, documented, and linked to the checklist.  

**Author**: Paola Holguín  
