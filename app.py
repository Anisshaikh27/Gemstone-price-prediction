from flask import Flask,request,render_template,jsonify

from src.pipeline.prediction_pipeline import PredictPipeline,CustomData
import os
from datetime import datetime
app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_datapoint():
    if request.method == "POST":
        try:
            # Handle JSON data from the frontend
            if request.is_json:
                json_data = request.get_json()
                data = CustomData(
                    carat=float(json_data.get("carat")),
                    depth=float(json_data.get("depth")),
                    table=float(json_data.get("table")),
                    x=float(json_data.get("x")),
                    y=float(json_data.get("y")),
                    z=float(json_data.get("z")),
                    cut=json_data.get("cut"),
                    color=json_data.get("color"),
                    clarity=json_data.get("clarity")
                )
            else:
                # Handle form data (fallback)
                data = CustomData(
                    carat=float(request.form.get("carat")),
                    depth=float(request.form.get("depth")),
                    table=float(request.form.get("table")),
                    x=float(request.form.get("x")),
                    y=float(request.form.get("y")),
                    z=float(request.form.get("z")),
                    cut=request.form.get("cut"),
                    color=request.form.get("color"),
                    clarity=request.form.get("clarity")
                )
            
            final_data = data.get_data_as_dataframe()
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_data)
            result = round(pred[0], 2)
            
            return jsonify({
                'price': round(result, 2),
                'status': 'success',
                'timestamp': str(datetime.now())
            })
            
        except ValueError as e:
            return jsonify({
                'status': 'error',
                'error': f'Invalid input data: {str(e)}'
            }), 400
        except Exception as e:
            return jsonify({
                'status': 'error',
                'error': f'Prediction failed: {str(e)}'
            }), 500
    else:
        return jsonify({'status': 'error', 'message': 'Invalid request method'}), 405

@app.route('/health')
def health_check():
    """Health check endpoint for Docker and Render"""
    return {
        'status': 'healthy',
        'timestamp': str(datetime.now()),
        'version': '1.0.0',
        'environment': os.getenv('FLASK_ENV', 'development')
    }, 200

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return {
        'status': 'running',
        'service': 'gemstone-price-predictor',
        'docker': True,
        'version': '1.0.0'
    }

# Add error handlers
@app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    return {'error': 'Internal server error'}, 500



# Update your main section for production
if __name__ == "__main__":
    # Get port from environment (Render sets this)
    port = int(os.getenv('PORT', 5000))
    
    # Check if running in production
    debug = os.getenv('FLASK_ENV') != 'production'
    
    print(f"🚀 Starting Flask app on port {port}")
    print(f"🔧 Debug mode: {debug}")
    print(f"🌍 Environment: {os.getenv('FLASK_ENV', 'development')}")
    
    # Run the app
    app.run(host='0.0.0.0', port=port, debug=debug)