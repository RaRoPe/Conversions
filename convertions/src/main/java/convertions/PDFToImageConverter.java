package convertions;


import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.rendering.PDFRenderer;
import org.apache.pdfbox.rendering.ImageType;

import javax.imageio.ImageIO;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.filechooser.FileSystemView;
import java.awt.image.BufferedImage;
import java.io.File;

public class PDFToImageConverter {
	public static void main(String[] args) {
		try {
			// File selector to user choose where the PDF file is
			JFileChooser fileChooser = new JFileChooser(FileSystemView.getFileSystemView().getHomeDirectory());
			fileChooser.setFileFilter(new FileNameExtensionFilter("Files PDF", "pdf"));
			fileChooser.setDialogTitle("Open PDF File");

			int result = fileChooser.showOpenDialog(null);

			if (result == JFileChooser.APPROVE_OPTION) {
				File pdfFile = fileChooser.getSelectedFile();

				// Selector for output directory
				JFileChooser dirChooser = new JFileChooser(FileSystemView.getFileSystemView().getHomeDirectory());
				dirChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
				dirChooser.setDialogTitle("Output folder");

				int dirResult = dirChooser.showOpenDialog(null);

				if (dirResult == JFileChooser.APPROVE_OPTION) {
					File outputDir = dirChooser.getSelectedFile();

					String[] formats = { "JPG", "PNG" };
					int formatChoice = JOptionPane.showOptionDialog(null, "Choose the output images format:",
							"Output format", JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE, null, formats,
							formats[0]);

					// "jpg" or "png"
					String format = formats[formatChoice].toLowerCase();

					// Load PDF file
					PDDocument document = PDDocument.load(pdfFile);

					// Object of type PDFRenderer to page's rendering
					PDFRenderer renderer = new PDFRenderer(document);

					for (int page = 0; page < document.getNumberOfPages(); page++) {
						// Render the page as a image of type BufferedImage
						BufferedImage image = renderer.renderImageWithDPI(page, 300, ImageType.RGB);

						// Output file name
						String outputFileName = pdfFile.getName() + "_page_" + (page + 1) + "." + format;

						// Images output path
						File outputFile = new File(outputDir, outputFileName);

						// Save the image in the format that was chosen by user in the chosen path
						ImageIO.write(image, format, outputFile);
						
						System.out.println("Converting page "+(page+1)+"/"+document.getNumberOfPages());
					}

					// Close the document to release the resources
					document.close();

					System.out.println("Conversion finished.");
				} else {
					System.out.println("None folder was selected.");
				}
			} else {
				System.out.println("No PDF file was selected.");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}

