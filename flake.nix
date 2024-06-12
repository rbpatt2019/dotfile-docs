{
  description = "Building docs with sphinx";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, flake-utils, nixpkgs }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        sphinx = pkgs.python312.withPackages (pp: [
            pp.sphinx-tabs
            pp.sphinx-book-theme
            pp.pyenchant
            pp.sphinx-autobuild
        ]);
      in
      {
        # nix shell
        packages = {
          default = pkgs.buildEnv {
            name = "sphinx-dev";
            paths = [ sphinx ];
          };
          autobuild = pkgs.buildEnv {
            name = "sphinx-autobuild";
            paths = [
              (pkgs.writeShellApplication {
                name = "sphinx-autobuild";
                text = ''
                  ${sphinx}/bin/sphinx-autobuild "$@"
                '';
                runtimeInputs = [ sphinx ];
              })
            ];
          };
          build = pkgs.buildEnv {
            name = "sphinx-build";
            paths = [
              (pkgs.writeShellApplication {
                name = "sphinx-build";
                text = ''
                  ${sphinx}/bin/sphinx-build "$@"
                '';
                runtimeInputs = [ sphinx ];
              })
            ];
          };
        };

        # nix develop
        devShells.default = pkgs.mkShell {
          name = "sphinx-dev";
          buildInputs = [ sphinx ];
        };
      }
    );

}
