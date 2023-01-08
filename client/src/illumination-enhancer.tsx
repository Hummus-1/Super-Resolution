import { ImageForm } from "./components/image-form";
import { Navbar } from "./components/navigation/navbar";
import "./illumination-enhancer.scss";

const IlluminationEnhancerForm = () => {
  return ImageForm({
    processingLink: "http://localhost:8000/enhance/light",
    imageWidth: 256,
    imageHeight: 256,
    imageSize: 250_000,
  });
};

function IlluminationEnhancer() {
  return (
    <div className="IlluminationEnhancer">
      <link
        href="https://fonts.googleapis.com/css?family=Lexend"
        rel="stylesheet"
      />
      <Navbar />
      <IlluminationEnhancerForm />
    </div>
  );
}

export default IlluminationEnhancer;
