pyinstaller --name="PDF转化图片" \
            --windowed \
            --onefile \
            --icon="/Users/EvelynZhang/Desktop/PDFToImagesApp/IconSet.icns" \
         		PDF转化图片.py

create-dmg \
  --volname "PDF转化图片" \
  --icon "PDF转化图片" 150 150 \
  --app-drop-link 350 150 \
  "PDF转化图片.dmg" \
  "dist/"

