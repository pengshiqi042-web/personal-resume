import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // 如果使用 GitHub Pages，需要取消注释并设置 base 路径
  // base: '/仓库名/',
})




