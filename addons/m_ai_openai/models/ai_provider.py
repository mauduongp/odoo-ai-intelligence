from odoo import fields, models
import openai

class AiProviderOpenAI(models.Model):
    _inherit = 'm_ai.provider'

    provider_type = fields.Selection(selection_add=[('openai', 'OpenAI')])

    def _get_response_openai(self, prompt, system_prompt, model_code):
        """
        Get response from OpenAI
        """
        self.ensure_one()
        client = openai.OpenAI(api_key=self.api_key, base_url=(self.base_url or None))
        response = client.chat.completions.create(
            model=model_code,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
