<template>
    <div class="w-full max-w-xl mx-auto p-6">
      <div
        :class="[
          'relative rounded-lg border-2 border-dashed p-8 transition-all',
          dragActive ? 'border-blue-500 bg-blue-50' : 'border-gray-300',
          file ? 'bg-green-50' : 'bg-white'
        ]"
        @dragenter="handleDrag"
        @dragleave="handleDrag"
        @dragover="handleDrag"
        @drop="handleDrop"
      >
        <input
          ref="inputRef"
          type="file"
          class="hidden"
          accept=".txt"
          @change="handleChange"
        />
  
        <div class="flex flex-col items-center justify-center space-y-4">
          <template v-if="!file">
            <Upload :class="`w-12 h-12 ${dragActive ? 'text-blue-500' : 'text-gray-400'}`" />
            <div class="text-center">
              <p class="text-lg font-medium text-gray-700">Drop your WhatsApp backup file here</p>
              <p class="text-sm text-gray-500">or click to select a file</p>
            </div>
            <button
              @click="handleButtonClick"
              class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600
                transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 
                focus:ring-offset-2"
            >
              Select File
            </button>
          </template>
  
          <template v-else>
            <CheckCircle class="w-12 h-12 text-green-500" />
            <div class="flex items-center space-x-2">
              <FileText class="w-5 h-5 text-gray-500" />
              <span class="text-gray-700 font-medium">{{ file.name }}</span>
            </div>
            <button
              @click="removeFile"
              class="px-4 py-2 bg-gray-100 text-gray-700 rounded-md 
                hover:bg-gray-200 transition-colors"
            >
              Remove
            </button>
          </template>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { Upload, FileText, CheckCircle, AlertCircle } from 'lucide-vue-next';
  
  const dragActive = ref(false);
  const file = ref(null);
  const error = ref('');
  const inputRef = ref(null);
  
  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragActive.value = e.type === 'dragenter' || e.type === 'dragover';
  };
  
  const validateFile = (selectedFile) => {
    if (!selectedFile.name.endsWith('.txt')) {
      error.value = 'Please upload a valid WhatsApp chat backup file (.txt)';
      return false;
    }
    if (selectedFile.size > 10 * 1024 * 1024) { // 10MB limit
      error.value = 'File size should be less than 10MB';
      return false;
    }
    return true;
  };
  
  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragActive.value = false;
    error.value = '';
  
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile && validateFile(droppedFile)) {
      file.value = droppedFile;
    }
  };
  
  const handleChange = (e) => {
    error.value = '';
    const selectedFile = e.target.files[0];
    if (selectedFile && validateFile(selectedFile)) {
      file.value = selectedFile;
    }
  };
  
  const handleButtonClick = () => {
    inputRef.value.click();
  };
  
  const removeFile = () => {
    file.value = null;
  };
  </script>
  
  <style scoped>
  /* Add any necessary styling adjustments */
  </style>
  