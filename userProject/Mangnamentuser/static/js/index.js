const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

const container = document.getElementById('three-container');

if (container) {
    
    renderer.setSize(window.innerWidth, window.innerHeight);

    container.appendChild(renderer.domElement);
    
    window.addEventListener('resize', () => {
        const newWidth = window.innerWidth;
        const newHeight = window.innerHeight;

        camera.aspect = newWidth / newHeight;
        camera.updateProjectionMatrix();

        renderer.setSize(newWidth, newHeight);
        
    });

    // Carga de texturas
    const textureLoader = new THREE.TextureLoader();

    const baseColorMap = textureLoader.load('/static/images/textures/Lapis_Lazuli_001_COLOR.jpg');
    const displacementMap = textureLoader.load('/static/images/textures/Lapis_Lazuli_001_DISP.png');
    const normalMap = textureLoader.load('/static/images/textures/Lapis_Lazuli_001_NORM.jpg');
    const occlusionMap = textureLoader.load('/static/images/textures/Lapis_Lazuli_001_OCC.jpg');
    const roughnessMap = textureLoader.load('/static/images/textures/Lapis_Lazuli_001_ROUGH.jpg');
    baseColorMap.minFilter = THREE.NearestFilter;

    // Creación de material PBR
    const material = new THREE.MeshStandardMaterial({
        map: baseColorMap,
        displacementMap: displacementMap,
        normalMap: normalMap,
        aoMap: occlusionMap,
        roughnessMap: roughnessMap,
        emissiveIntensity: 0.4,
        roughness: 0.5,
        metalness: 0.5,
    });

    // Creación de una esfera (representando el planeta)
    const geometry = new THREE.SphereGeometry(5, 32, 32);
    const planet = new THREE.Mesh(geometry, material);

    scene.add(planet);
    camera.position.z = 15;

    // Agregar iluminación
    const ambientLight = new THREE.AmbientLight(0x404040); // Luz ambiental
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 1); // Luz direccional
    directionalLight.position.set(5, 5, 5);
    scene.add(directionalLight);

    // Animación de rotación del planeta
    const animate = function () {
        requestAnimationFrame(animate);
        planet.rotation.y += 0.005;
        renderer.render(scene, camera);
    };

    animate();
} else {
    console.error("Container element not found!");
}
