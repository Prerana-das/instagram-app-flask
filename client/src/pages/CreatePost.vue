<template>
  <LayoutWrapper>
    <div class=" bg-black text-white min-h-screen max-w-2xl mx-auto py-10 px-6">
      <h2 class="text-2xl font-semibold mb-6 text-center">Create New Post</h2>
      <form @submit.prevent="handleSubmit" class="space-y-5">
        <!-- File Upload -->
        <div>
          <label class="block text-sm font-medium mb-1">Upload Image or Video</label>
          <input type="file" accept="image/*,video/*" @change="handleFileUpload" class="file-input w-full" />
          <p v-if="fileName" class="text-sm text-gray-500 mt-1">{{ fileName }}</p>
        </div>
        <!-- Caption -->
        <div>
          <label class="block text-sm font-medium mb-1">Caption</label>
          <textarea rows="4" v-model="form.caption" class="form-field" placeholder="Write a caption..."></textarea>
        </div>

        <!-- Location -->
        <div>
          <label class="block text-sm font-medium mb-1">Location</label>
            <input
              v-model="form.location"
              type="text"
              class="form-field"
              placeholder="Add a location"
            />
        </div>

        <!-- Submit Button -->
        <div class="text-center">
            <button
              type="submit"
              class="w-full bg-red-600 hover:bg-red-700 text-white font-semibold py-2 px-4 rounded-lg transition-colors duration-200"
            >
              Post
            </button>
          </div>
      </form>
    </div>
  </LayoutWrapper>
</template>

<script setup>
import { ref } from 'vue'
import LayoutWrapper from '@/components/Layout/LayoutWrapper.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  caption: '',
  location: ''
})

const file = ref(null)
const fileName = ref('')

function handleFileUpload(event) {
  const uploadedFile = event.target.files[0]
  if (uploadedFile && (uploadedFile.type.startsWith('image/') || uploadedFile.type.startsWith('video/'))) {
    file.value = uploadedFile
    fileName.value = uploadedFile.name
  } else {
    alert('Please upload a valid image or video file.')
  }
}

async function handleSubmit() {
  if (!file.value) {
    alert('Please select a file.')
    return
  }

  const formData = new FormData()
  formData.append('caption', form.value.caption)
  formData.append('location', form.value.location)
  formData.append('file', file.value)
  formData.append('user_id', 1)  // hardcoded user for now

  const res = await fetch('/api/posts', {
    method: 'POST',
    body: formData,
  })

  const data = await res.json()
  if (res.ok) {
    alert('Post uploaded!')
    form.value.caption = ''
    form.value.location = ''
    file.value = null
    fileName.value = ''
    router.push('/') 
  } else {
    alert('Error: ' + data.error)
  }
}

</script>
