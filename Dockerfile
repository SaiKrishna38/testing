# Use the official AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.12

# Copy application code
COPY app.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the Lambda handler
CMD ["app.lambda_handler"]
