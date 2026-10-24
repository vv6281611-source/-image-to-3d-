
import gradio as gr

def process_image(image):
    if image is None:
        return "पहले एक फोटो चुनें।"
    return (
        "फोटो सफलतापूर्वक प्राप्त हुई है। "
        "असली Image-to-3D AI मॉडल अभी जोड़ना बाकी है।"
    )

demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil", label="अपनी फोटो चुनें"),
    outputs=gr.Textbox(label="स्थिति"),
    title="My AI Image to 3D",
    description="मुफ्त Image-to-3D प्रोटोटाइप"
)

if __name__ == "__main__":
    demo.launch()
