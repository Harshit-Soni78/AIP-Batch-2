document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const previewSection = document.getElementById('previewSection');
    const imagePreview = document.getElementById('imagePreview');
    const videoPreview = document.getElementById('videoPreview');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const resetBtn = document.getElementById('resetBtn');
    const resultSection = document.getElementById('resultSection');
    const detectionResult = document.getElementById('detectionResult');
    const confidenceFill = document.getElementById('confidenceFill');
    const confidenceScore = document.getElementById('confidenceScore');

    let currentFile = null;

    // Drag and drop handlers
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = '#4299e1';
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.style.borderColor = '#cbd5e0';
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = '#cbd5e0';
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFile(files[0]);
        }
    });

    // Click to upload
    dropZone.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });

    // Handle file selection
    function handleFile(file) {
        if (!file.type.match('image.*') && !file.type.match('video.*')) {
            alert('Please upload an image or video file');
            return;
        }

        currentFile = file;
        previewSection.style.display = 'block';
        resultSection.style.display = 'none';

        if (file.type.match('image.*')) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                imagePreview.style.display = 'block';
                videoPreview.style.display = 'none';
            };
            reader.readAsDataURL(file);
        } else if (file.type.match('video.*')) {
            const reader = new FileReader();
            reader.onload = (e) => {
                videoPreview.src = e.target.result;
                videoPreview.style.display = 'block';
                imagePreview.style.display = 'none';
            };
            reader.readAsDataURL(file);
        }
    }

    // Analyze button handler
    analyzeBtn.addEventListener('click', async () => {
        if (!currentFile) return;

        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = '<span class="loading"></span> Analyzing...';
        detectionResult.textContent = 'Processing...';
        confidenceFill.style.width = '0%';
        confidenceScore.textContent = '0%';

        const formData = new FormData();
        formData.append('file', currentFile);

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            
            // Update results
            resultSection.style.display = 'block';
            detectionResult.textContent = result.is_deepfake ? 'Deepfake Detected' : 'Authentic';
            detectionResult.style.color = result.is_deepfake ? '#e53e3e' : '#38a169';
            
            const confidence = Math.round(result.confidence * 100);
            confidenceFill.style.width = `${confidence}%`;
            confidenceScore.textContent = `${confidence}%`;
        } catch (error) {
            console.error('Error:', error);
            detectionResult.textContent = 'Error analyzing file';
            detectionResult.style.color = '#e53e3e';
        } finally {
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = 'Analyze';
        }
    });

    // Reset button handler
    resetBtn.addEventListener('click', () => {
        currentFile = null;
        fileInput.value = '';
        imagePreview.src = '';
        videoPreview.src = '';
        previewSection.style.display = 'none';
        resultSection.style.display = 'none';
    });
}); 