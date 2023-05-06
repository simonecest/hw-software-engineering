// / < summary >
// / Get the camera image and save it as a JPG
// / < / summary >
// / < param
name = "m_Camera" > Designated cameras < / param >
// / < param
name = "filename" > Image naming < / param >
void
CameraCapture(Camera
m_Camera, string
filename)
{
// Get the camera
RenderTexture
rt = new
RenderTexture(800, 800, 16);
m_Camera.targetTexture = rt;
m_Camera.Render();
RenderTexture.active = rt;
Texture2D
t = new
Texture2D(800, 800);
t.ReadPixels(new
Rect(0, 0, t.width, t.height), 0, 0);
t.Apply();

// Save image
string[]
ss = Application.dataPath.Split("/");
string
path = "";
for (int i = 0; i < ss.Length - 1; i++)
{
    path += ss[i] + "/";
}

string
filePath = path + "/RecMap/" + filename + ".jpg";
System.IO.File.WriteAllBytes(filePath, t.EncodeToJPG());
m_Camera.targetTexture = null;

}