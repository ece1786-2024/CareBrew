scenarios = {
    "Delayed Service & Slow Response": [
        {
            "issue": "Delayed Service Response",
            "description": "Customers are waiting too long for their orders to be taken or served.",
            "factors_involved": ["Trust and Reactivity (Responding immediately to customer's question)", "Taste (Taste of beverages)"],
            "possible_cause": "Slow response time or lack of urgency from staff."
        },
        {
            "issue": "Customer Uncertainty About Service Timing",
            "description": "Customers are unsure when their order will be ready, leading to frustration.",
            "factors_involved": ["Trust and Reactivity (Providing rapid service in order of visiting customer)", "Materiality (Facilities and equipment)"],
            "possible_cause": "Inefficient systems for communicating order wait times."
        },
        {
            "issue": "Slow or Inaccurate Order Fulfillment",
            "description": "Orders are either delayed or wrong, leading to dissatisfaction.",
            "factors_involved": ["Trust and Reactivity (Responding immediately to customer's question)", "Materiality (Attire and appearance of workers)"],
            "possible_cause": "Errors in the order-taking process, kitchen or barista mistakes, or understaffing."
        }
    ],
    
    "Staff Interaction & Customer Engagement": [
        {
            "issue": "Unfriendly or Unhelpful Staff",
            "description": "Customers feel that the staff is not friendly or helpful, making them uncomfortable.",
            "factors_involved": ["Assurance and Sympathy (Being friendly and thoughtful)", "Trust and Reactivity (Attitude to help customers willingly)"],
            "possible_cause": "Staff may be disengaged, not trained to be empathetic, or simply overworked."
        },
        {
            "issue": "Staff Ignoring or Not Listening to Customer Requests",
            "description": "Customers’ specific requests or preferences are ignored by staff.",
            "factors_involved": ["Trust and Reactivity (Treating customer's demand accurately)", "Assurance and Sympathy (Understanding customer's needs and emotion)"],
            "possible_cause": "Miscommunication, inattentive staff, or lack of training."
        },
        {
            "issue": "Lack of Personalization in Service",
            "description": "Customers feel that the service lacks personal touch and doesn't cater to their individual preferences.",
            "factors_involved": ["Assurance and Sympathy (Deep interest towards individual customers)", "Trust and Reactivity (Treating customer's demand accurately)"],
            "possible_cause": "Staff fails to engage with customers or doesn't offer tailored recommendations."
        }
    ],
    
    "Food & Beverage Quality": [
        {
            "issue": "Inconsistent Quality of Food or Beverage",
            "description": "The taste or quality of beverages and food items is inconsistent from visit to visit.",
            "factors_involved": ["Taste (Taste of beverages)", "Materiality (Physical Environment)"],
            "possible_cause": "Issues with ingredient quality, inconsistent preparation, or lack of standardization."
        },
        {
            "issue": "Unpleasant Taste of Beverages or Food",
            "description": "Customers find the taste of their beverages or food unpleasant, which diminishes their experience.",
            "factors_involved": ["Taste (Taste of beverages)", "Materiality (Facilities and equipment)"],
            "possible_cause": "Poor ingredient quality, improper preparation, or an error in the recipe."
        },
        {
            "issue": "Temperature Issues with Coffee or Food",
            "description": "Customers receive beverages or food that are either too hot or too cold.",
            "factors_involved": ["Taste (Taste of coffee)", "Trust and Reactivity (Providing rapid service in order of visiting customer)"],
            "possible_cause": "Temperature control issues, equipment malfunction, or poor timing."
        }
    ],
    
    "Physical Environment & Cleanliness": [
        {
            "issue": "Dirty or Unappealing Store Environment",
            "description": "The physical environment of the store (e.g., cleanliness, décor, or maintenance) is uninviting or dirty.",
            "factors_involved": ["Materiality (Store atmosphere including interior)", "Assurance and Sympathy (Trust towards hygiene and safety)"],
            "possible_cause": "Lack of regular cleaning or outdated equipment and décor."
        },
        {
            "issue": "Unprofessional or Unkempt Appearance of Staff",
            "description": "Employees' attire or appearance doesn't meet hygiene or professionalism standards.",
            "factors_involved": ["Materiality (Attire and appearance of workers)", "Assurance and Sympathy (Being safe from all situations such as fire)"],
            "possible_cause": "Lack of proper uniforms, poor grooming standards, or failure to maintain hygiene protocols."
        },
        {
            "issue": "Inadequate Allergy or Dietary Information",
            "description": "The menu doesn't provide enough information about allergens or dietary restrictions (e.g., gluten-free, vegan).",
            "factors_involved": ["Assurance and Sympathy (Understanding customer's needs and emotion)", "Taste (Taste of beverages)"],
            "possible_cause": "Lack of clear labeling or communication regarding food allergies."
        },
        {
            "issue": "Substandard Hygiene or Safety Practices",
            "description": "Customers feel uncomfortable due to a lack of visible hygiene or safety measures (e.g., staff not wearing gloves, unclean bathrooms).",
            "factors_involved": ["Assurance and Sympathy (Trust towards hygiene and safety)", "Materiality (Physical Environment)"],
            "possible_cause": "Inadequate cleaning schedules or failure to meet safety regulations."
        }
    ],

    "Customer Expectations & Service Communication": [
        {
            "issue": "Confusing Loyalty Program or Promotions",
            "description": "Customers have trouble understanding or using the store's loyalty program or promotions.",
            "factors_involved": ["Trust and Reactivity (Keeping promise made by customers)", "Materiality (Physical Environment)"],
            "possible_cause": "Complex or unclear promotion rules, or staff unfamiliar with the program."
        },
        {
            "issue": "Misleading or Unclear Pricing",
            "description": "Customers are confused or upset by pricing, especially if the menu does not match the final bill.",
            "factors_involved": ["Materiality (Physical Environment)", "Trust and Reactivity (Keeping promise made by customers)"],
            "possible_cause": "Menu prices not updated or hidden fees on the final bill."
        },
        {
            "issue": "Unclear Communication of Menu Choices",
            "description": "Customers are unsure of the menu options or ingredients in their beverages/food.",
            "factors_involved": ["Assurance and Sympathy (Deep interest towards individual customers)", "Materiality (Store atmosphere including interior)"],
            "possible_cause": "Lack of clear signage or insufficient communication from staff."
        },
        {
            "issue": "Unclear or Unfriendly Return/Refund Process",
            "description": "Customers encounter frustration when attempting to return or exchange products (e.g., if something is wrong with their order).",
            "factors_involved": ["Assurance and Sympathy (Carrying out service with sympathy)", "Trust and Reactivity (Responding immediately to customer's question)"],
            "possible_cause": "Unclear policies or reluctance from staff to address issues."
        }
    ]
}

customer_types = ["Regular customer", "New customer", "Walk-in customer", "Online order customer", "Returning customer"]

cause_type = ["Customer induced issue", "Communication induced error", "Employee induced error", "IT induced error", "Accidental issue"]