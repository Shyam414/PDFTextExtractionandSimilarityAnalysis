import tensorflow as tf
from transformers import BertTokenizer, TFBertForQuestionAnswering
from tqdm import tqdm
from pdfextract import PDFExtract

class QAModelTF:
    def __init__(self, model_name="bert-base-uncased"):
        self.model_name = model_name
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = TFBertForQuestionAnswering.from_pretrained(model_name)

    def tokenize(self, context, question):
        inputs = self.tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="tf")
        return inputs

    def train(self, train_dataset, epochs=3, batch_size=8, learning_rate=2e-5):
        optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
        train_loader = tf.data.Dataset.from_tensor_slices(train_dataset).batch(batch_size)

        for epoch in range(epochs):
            total_loss = 0.0
            for batch in tqdm(train_loader, desc="Epoch {}".format(epoch + 1)):
                inputs = {key: tf.convert_to_tensor(value) for key, value in batch.items()}
                with tf.GradientTape() as tape:
                    outputs = self.model(inputs)
                    loss = outputs.loss
                gradients = tape.gradient(loss, self.model.trainable_variables)
                optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))
                total_loss += loss.numpy()
            print("Epoch {} Loss: {:.4f}".format(epoch + 1, total_loss / len(train_loader)))

    def predict(self, context, question):
        inputs = self.tokenize(context, question)
        outputs = self.model(inputs)
        start_scores, end_scores = outputs.start_logits, outputs.end_logits
        start_index = tf.argmax(start_scores, axis=1).numpy()[0]
        end_index = tf.argmax(end_scores, axis=1).numpy()[0]
        input_ids = inputs['input_ids'].numpy()[0]
        answer_tokens = input_ids[start_index:end_index + 1]
        answer = self.tokenizer.decode(answer_tokens)
        return answer

# Example usage:
if __name__ == "__main__":
    pdf_path = "your_pdf_file.pdf"
    pdf_processor = PDFExtract()
    texts = pdf_processor.process_pdf(pdf_path)

    model = QAModelTF()
    context = " ".join(texts)
    question = "What is the main subject of this document?"
    answer = model.predict(context, question)
    print("Question:", question)
    print("Answer:", answer)
