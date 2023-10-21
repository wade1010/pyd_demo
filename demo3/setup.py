from distutils.core import setup, Extension

def main():
    setup(name="myadd",
          version="1.0.0",
          description="Python interface for the myadd C library function",
          author="Nadiah",
          author_email="nadiah@nadiah.org",
          ext_modules=[Extension("myadd", sources=["myadd.cpp"],extra_compile_args=['/Zi'],extra_link_args=['/DEBUG'])],
          )


if __name__ == "__main__":
    main()