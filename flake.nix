{
  description = "amsatop devshell environment is set up, so Pablo is happy and can run it on his computer 🥶";

  inputs.nixpkgs = {
    url = "github:nixos/nixpkgs/nixos-unstable?shallow=1";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";  # or "aarch64-darwin" etc. depending on your system
      pkgs = import nixpkgs {
        inherit system; 
        config.allowUnfree = true;
      };
      pythonEnv = pkgs.python313.withPackages (ps: with ps; [
          sphinx
          sphinx-rtd-theme
          myst-parser     # optional: markdown support
          pyfiglet
          textual
        ]);
        real_file = ''
            amsatop package
            ===============
            
            Library 
            ---------------
            
            .. automodule:: amsatop
               :members:
               :show-inheritance:
               :undoc-members:
            
            
            Utilities
            -----------
            
            .. toctree::
               :maxdepth: 4
            
               amsatop.utils
        '';
    in {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [ pkgs.uv ];
      };
       packages.${system}.default = pkgs.stdenv.mkDerivation {
        pname = "amsatop-docs";
        version = "1.0";

        src = ./.;

        nativeBuildInputs = [ pythonEnv ];

        buildPhase = ''
          sphinx-apidoc -o docs/_apidoc src/amsatop
          cat > docs/_apidoc/amsatop.rst << EOF 
          ${real_file} 
          EOF
          sphinx-build -b html docs/ build/
        '';

        installPhase = ''
          mkdir -p $out
          cp -r build/* $out/
        '';
      };
    };
}
