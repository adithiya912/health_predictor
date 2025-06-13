const { exec } = require('child_process');
const path = require('path');

async function predictHeartDisease(inputData) {
  return new Promise((resolve, reject) => {
    // Get the absolute path to the predict.py script
    const pythonScriptPath = path.join(__dirname, 'predict.py');
    
    // Execute the Python script
    const pythonProcess = exec(
      `python "${pythonScriptPath}"`,
      { stdio: ['pipe', 'pipe', 'pipe'] }
    );

    // Handle errors in starting the process
    pythonProcess.on('error', (err) => {
      reject(new Error(`Failed to start Python process: ${err.message}`));
    });

    // Send input data to Python process
    pythonProcess.stdin.write(JSON.stringify(inputData));
    pythonProcess.stdin.end();

    let result = '';
    let errorOutput = '';

    // Collect data from Python stdout
    pythonProcess.stdout.on('data', (data) => {
      result += data.toString();
    });

    // Collect errors from Python stderr
    pythonProcess.stderr.on('data', (data) => {
      errorOutput += data.toString();
    });

    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        console.error(`Python process exited with code ${code}`);
        console.error(`Error output: ${errorOutput}`);
        reject(new Error(`Prediction failed with code ${code}: ${errorOutput}`));
      } else {
        try {
          const parsedResult = JSON.parse(result);
          if (parsedResult.error) {
            reject(new Error(parsedResult.error));
          } else {
            resolve(parsedResult);
          }
        } catch (err) {
          console.error('Failed to parse Python output:', result);
          reject(new Error('Failed to parse prediction result'));
        }
      }
    });
  });
}

module.exports = { predictHeartDisease };