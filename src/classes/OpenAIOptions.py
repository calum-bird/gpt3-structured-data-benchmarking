class OpenAIOptions:
  def __init__(self, model: str, max_length: int, temperature: float, top_p: float, stop_sequence: list[str]):
    self.model = model
    self.max_length = max_length
    self.temperature = temperature
    self.top_p = top_p
    self.stop_sequence = stop_sequence